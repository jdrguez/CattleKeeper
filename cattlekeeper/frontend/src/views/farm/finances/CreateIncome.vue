<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import api from '@/api/axios';

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
  }
};

onMounted(() => {
  fetchBatches();
});

const createIncome = async () => {
  try {
    await api.post('api/farm/finances/incomes/create/', form.value);
    alert('Ingreso creado correctamente');
    router.push({ name: 'incomes' });
  } catch (error) {
    console.error('Error creando ingreso:', error);
    alert('Hubo un error al crear el ingreso.');
  }
};
</script>

<template>
  <div>
    <h1>Crear Ingreso</h1>
    <form @submit.prevent="createIncome">
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
          <option value="" disabled selected>Selecciona un lote</option>
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
        <input v-model="form.amount" type="number" required placeholder="Monto" />
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

      <button type="submit">Crear Ingreso</button>
    </form>
  </div>
</template>
