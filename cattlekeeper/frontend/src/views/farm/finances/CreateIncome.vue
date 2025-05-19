<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import api from '@/api/axios';
import { useToast } from 'vue-toastification';

const toast = useToast();
const router = useRouter();

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

const fetchBatches = async () => {
  try {
    const response = await api.get('api/farm/batch/');
    batches.value = response.data;
  } catch (error) {
    console.error('Error al obtener lotes:', error);
    toast.error('No se pudieron cargar los lotes');
  }
};

onMounted(() => {
  fetchBatches();
});

const createIncome = async () => {
  try {
    await api.post('api/farm/finances/incomes/create/', form.value);
    toast.success('Ingreso creado correctamente');
    router.push({ name: 'incomes' });
  } catch (error) {
    console.error('Error creando ingreso:', error);
    toast.error('Hubo un error al crear el ingreso');
  }
};
</script>

<template>
  <div class="container mt-5">
    <div class="card shadow-sm">
      <div class="card-header bg-success text-white">
        <h2 class="mb-0">Crear ingreso</h2>
      </div>
      <div class="card-body">
        <form @submit.prevent="createIncome">
          <div class="row g-3">

            <div class="col-md-6">
              <label class="form-label">Categoría <span class="text-danger">*</span></label>
              <select v-model="form.category" class="form-select" required>
                <option value="" disabled>Seleccionar categoría...</option>
                <option v-for="option in categories" :key="option.value" :value="option.value">
                  {{ option.label }}
                </option>
              </select>
            </div>

            <div class="col-md-6">
              <label class="form-label">Lote <span class="text-danger">*</span></label>
              <select v-model="form.batch" class="form-select" required>
                <option value="" disabled>Seleccionar lote...</option>
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
                rows="4"
                required
                placeholder="Detalles del ingreso..."
              ></textarea>
            </div>

            <div class="col-md-4">
              <label class="form-label">Monto <span class="text-danger">*</span></label>
              <input
                type="number"
                v-model="form.amount"
                class="form-control"
                min="0.01"
                step="0.01"
                required
              />
            </div>

            <div class="col-md-4">
              <label class="form-label">Fecha <span class="text-danger">*</span></label>
              <input
                type="date"
                v-model="form.date"
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
            <button
              type="button"
              class="btn btn-secondary me-2"
              @click="$router.back()"
            >
              Cancelar
            </button>
            <button type="submit" class="btn btn-success">
              Crear Ingreso
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
