<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import api from '@/api/axios';

const router = useRouter();
const route = useRoute();
const batchSlug = ref(null);

onMounted(() => {
  if (route.params.batch_slug) {
    batchSlug.value = route.params.batch_slug;
  } else {
    console.error('El parámetro batch_slug no está disponible en la ruta');
  }
});

const form = ref({
  production_type: '',
  quantity: '',
  unit: '',
  date: '',
  notes: ''
});

const productionTypes = [
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

const createProduction = async () => {
  if (!batchSlug.value) {
    console.error('No se ha encontrado el batchSlug');
    return;
  }

  try {
    await api.post(`api/farm/batch/${batchSlug.value}/production/create/`, form.value);
    alert('Producción creada correctamente');
    router.push({ name: 'ProductionList', params: { batch_slug: batchSlug.value } });
  } catch (error) {
    console.error('Error creando producción:', error);
    alert('Hubo un error al crear la producción.');
  }
};
</script>

<template>
  <div>
    <h1>Crear Producción</h1>
    <form @submit.prevent="createProduction">
      <div>
        <label>Tipo de Producción:</label>
        <select v-model="form.production_type" required>
          <option v-for="option in productionTypes" :key="option.value" :value="option.value">
            {{ option.label }}
          </option>
        </select>
      </div>

      <div>
        <label>Cantidad:</label>
        <input type="number" v-model="form.quantity" required />
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
        <input type="date" v-model="form.date" required />
      </div>

      <div>
        <label>Notas:</label>
        <textarea v-model="form.notes" rows="3" />
      </div>

      <button type="submit">Crear Producción</button>
    </form>
  </div>
</template>
