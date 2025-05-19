<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import api from '@/api/axios';

const route = useRoute();
const router = useRouter();
const incomeId = route.params.id;

const form = ref({
  category: '',
  batch: '',
  description: '',
  amount: '',
  currency: '€',
  date: '',
});

const categories = [
  { value: 'SALE', label: 'Venta' },
  { value: 'SUBSIDY', label: 'Subvención' },
  { value: 'DONATION', label: 'Donación' },
  { value: 'OTHER', label: 'Otro' }
];

const batches = ref([]);

const fetchIncome = async () => {
  try {
    const response = await api.get('api/farm/finances/incomes/');
    const income = response.data.find(i => i.id == incomeId);
    if (!income) throw new Error('Ingreso no encontrado');
    form.value = {
      category: income.category,
      batch: income.batch?.slug || '',
      description: income.description,
      amount: income.amount,
      currency: income.currency,
      date: income.date,
    };
  } catch (error) {
    console.error('Error al cargar ingreso:', error);
    alert('No se pudo cargar el ingreso.');
    router.push({ name: 'all-incomes' });
  }
};

const fetchBatches = async () => {
  try {
    const response = await api.get('api/farm/batch/');
    batches.value = response.data;
  } catch (error) {
    console.error('Error al cargar lotes:', error);
  }
};

const updateIncome = async () => {
  try {
    await api.post(`api/farm/finances/incomes/${incomeId}/update/`, form.value);
    alert('Ingreso actualizado correctamente.');
    router.push({ name: 'incomes' });
  } catch (error) {
    console.error('Error actualizando ingreso:', error);
    alert('No se pudo actualizar el ingreso.');
  }
};

onMounted(() => {
  fetchIncome();
  fetchBatches();
});
</script>

<template>
  <div class="container mt-5" >
    <div class="card shadow-sm">
      <div class="card-header bg-success text-white">
        <h2 class="mb-0">Editar Ingreso</h2>
      </div>
      <div class="card-body">
        <form @submit.prevent="updateIncome">
          <div class="row g-3">

            <div class="col-md-6">
              <label class="form-label">Categoría <span class="text-danger">*</span></label>
              <select v-model="form.category" class="form-select" required>
                <option value="" disabled>Selecciona una categoría</option>
                <option v-for="option in categories" :key="option.value" :value="option.value">
                  {{ option.label }}
                </option>
              </select>
            </div>

            <div class="col-md-6">
              <label class="form-label">Lote <span class="text-danger">*</span></label>
              <select v-model="form.batch" class="form-select" required>
                <option value="" disabled>Selecciona un lote</option>
                <option v-for="batch in batches" :key="batch.slug" :value="batch.slug">
                  {{ batch.name || batch.slug }}
                </option>
              </select>
            </div>

            <div class="col-12">
              <label class="form-label">Descripción <span class="text-danger">*</span></label>
              <textarea
                v-model="form.description"
                class="form-control"
                rows="3"
                placeholder="Descripción"
                required
              ></textarea>
            </div>

            <div class="col-md-4">
              <label class="form-label">Monto <span class="text-danger">*</span></label>
              <input
                v-model="form.amount"
                type="number"
                min="0.01"
                step="0.01"
                class="form-control"
                required
              />
            </div>

            <div class="col-md-4">
              <label class="form-label">Fecha <span class="text-danger">*</span></label>
              <input
                v-model="form.date"
                type="date"
                class="form-control"
                required
              />
            </div>

            <div class="col-md-4">
              <label class="form-label">Moneda <span class="text-danger">*</span></label>
              <select v-model="form.currency" class="form-select" required>
                <option value="€">Euros (€)</option>
                <option value="$">Dólares ($)</option>
                <option value="">Otro</option>
              </select>
            </div>

          </div>

          <div class="mt-4 text-end">
            <button type="button" class="btn btn-secondary me-2" @click="router.back()">Cancelar</button>
            <button type="submit" class="btn btn-success">Guardar Cambios</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
