<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import api from '@/api/axios';

const route = useRoute();
const router = useRouter();
const batchSlug = route.params.batch_slug;
const productionPk = route.params.production_pk;

const form = ref({
  production_type: '',
  quantity: '',
  unit: '',
  date: '',
  notes: ''
});

// Predeterminados para tipo de producción y unidad
const productionTypeOptions = [
  { value: 'MEAT', label: 'Carne' },
  { value: 'MILK', label: 'Leche' },
  { value: 'EGG', label: 'Huevos' },
  { value: 'WOOL', label: 'Lana' }
];

const unitOptions = [
  { value: 'L', label: 'Litros' },
  { value: 'KG', label: 'Kilogramos' },
  { value: 'U', label: 'Unidades' }
];

onMounted(async () => {
  try {
    const res = await api.get(`api/farm/batch/${batchSlug}/production/`);
    const prod = res.data.find(p => p.id === parseInt(productionPk));
    if (prod) {
      form.value = {
        production_type: prod.production_type,
        quantity: prod.quantity,
        unit: prod.unit,
        date: prod.date,
        notes: prod.notes
      };
    }
  } catch (error) {
    console.error('Error cargando producción:', error);
  }
});

const updateProduction = async () => {
  try {
    await api.post(`api/farm/batch/${batchSlug}/production/${productionPk}/update/`, form.value);
    router.push({ name: 'ProductionList', params: { batch_slug: batchSlug } });
  } catch (error) {
    console.error('Error actualizando producción:', error);
  }
};
</script>

<template>
  <div>
    <h1>Editar Producción</h1>
    <form @submit.prevent="updateProduction">
      <div>
        <label>Tipo de Producción:</label>
        <select v-model="form.production_type" required>
          <option v-for="option in productionTypeOptions" :key="option.value" :value="option.value">
            {{ option.label }}
          </option>
        </select>
      </div>

      <div>
        <label>Cantidad:</label>
        <input v-model.number="form.quantity" type="number" required placeholder="Cantidad" />
      </div>

      <div>
        <label>Unidad:</label>
        <select v-model="form.unit" required>
          <option v-for="option in unitOptions" :key="option.value" :value="option.value">
            {{ option.label }}
          </option>
        </select>
      </div>

      <div>
        <label>Fecha:</label>
        <input v-model="form.date" type="date" required />
      </div>

      <div>
        <label>Notas:</label>
        <textarea v-model="form.notes" placeholder="Notas"></textarea>
      </div>

      <button type="submit">Actualizar</button>
    </form>
  </div>
</template>
