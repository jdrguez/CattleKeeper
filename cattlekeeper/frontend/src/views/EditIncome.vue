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
  <div>
    <h1>Editar Ingreso</h1>
    <form @submit.prevent="updateIncome">
      <div>
        <label>Categoría:</label>
        <select v-model="form.category" required>
          <option v-for="option in categories" :key="option.value" :value="option.value">
            {{ option.label }}
          </option>
        </select>
      </div>

      <div>
        <label>Lote:</label>
        <select v-model="form.batch" required>
          <option value="" disabled>Selecciona un lote</option>
          <option v-for="batch in batches" :key="batch.slug" :value="batch.slug">
            {{ batch.name || batch.slug }}
          </option>
        </select>
      </div>

      <div>
        <label>Descripción:</label>
        <textarea v-model="form.description" required placeholder="Descripción"></textarea>
      </div>

      <div>
        <label>Monto:</label>
        <input v-model="form.amount" type="number" required />
      </div>

      <div>
        <label>Fecha:</label>
        <input v-model="form.date" type="date" required />
      </div>

      <div>
        <label>Moneda:</label>
        <select v-model="form.currency" required>
          <option value="€">Euros</option>
          <option value="$">Dólares</option>
          <option value="">Otro</option>
        </select>
      </div>

      <button type="submit">Guardar Cambios</button>
    </form>
  </div>
</template>
