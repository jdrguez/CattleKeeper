<script setup>
import { ref } from 'vue';
import api from '@/api/axios';
import { useRouter } from 'vue-router';

const router = useRouter();

const form = ref({
  species: '',
  purchase_date: '',
  quantity: '',
  sex: 3, // Default: MIXED
  origin: '',
  notes: ''
});

const speciesOptions = [
  { value: 1, label: 'Cattle' },
  { value: 2, label: 'Poultry' },
  { value: 3, label: 'Pig' },
  { value: 4, label: 'Sheep' },
  { value: 5, label: 'Goat' },
  { value: 99, label: 'Other' }
];

const sexOptions = [
  { value: 1, label: 'Male' },
  { value: 2, label: 'Female' },
  { value: 3, label: 'Mixed' }
];

const createBatch = async () => {
  try {
    await api.post('api/farm/batch/create/', form.value);
    alert('Lote creado correctamente');
    router.push({ name: 'batch-list' });
  } catch (error) {
    console.error('Error al crear el lote:', error);
    alert('Hubo un error al crear el lote.');
  }
};
</script>

<template>
  <div>
    <h2>Crear nuevo lote</h2>
    <form @submit.prevent="createBatch">
      <div>
        <label>Especie:</label>
        <select v-model="form.species" required>
          <option v-for="option in speciesOptions" :key="option.value" :value="option.value">
            {{ option.label }}
          </option>
        </select>
      </div>

      <div>
        <label>Fecha de compra:</label>
        <input type="date" v-model="form.purchase_date" required />
      </div>

      <div>
        <label>Cantidad:</label>
        <input type="number" v-model="form.quantity" required />
      </div>

      <div>
        <label>Sexo:</label>
        <select v-model="form.sex">
          <option v-for="option in sexOptions" :key="option.value" :value="option.value">
            {{ option.label }}
          </option>
        </select>
      </div>

      <div>
        <label>Origen:</label>
        <input type="text" v-model="form.origin" />
      </div>

      <div>
        <label>Notas:</label>
        <textarea v-model="form.notes" rows="3" />
      </div>

      <button type="submit">Crear Lote</button>
    </form>
  </div>
</template>
