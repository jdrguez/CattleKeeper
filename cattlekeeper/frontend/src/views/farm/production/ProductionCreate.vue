<template>
  <div class="form-wrapper mx-auto p-5" style="max-width: 600px;">
    <h1 class="form-title mb-5">Crear Producción</h1>
    <form @submit.prevent="createProduction" class="form-grid">
      <div class="form-group">
        <label for="production_type">Tipo de Producción:</label>
        <select id="production_type" v-model="form.production_type" required>
          <option v-for="option in productionTypes" :key="option.value" :value="option.value">
            {{ option.label }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="quantity">Cantidad:</label>
        <input id="quantity" type="number" v-model="form.quantity" required placeholder="Cantidad" />
      </div>

      <div class="form-group">
        <label for="unit">Unidad:</label>
        <select id="unit" v-model="form.unit" required>
          <option v-for="option in unitOptions" :key="option.value" :value="option.value">
            {{ option.label }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="date">Fecha:</label>
        <input id="date" type="date" v-model="form.date" required />
      </div>

      <div class="form-group full-width">
        <label for="notes">Notas:</label>
        <textarea id="notes" v-model="form.notes" rows="3" placeholder="Notas"></textarea>
      </div>

      <button type="submit" class="btn-submit">Crear Producción</button>
    </form>
  </div>
</template>

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

<style scoped>
.form-wrapper {
  background: #ffffff;
  border-radius: 16px;
  box-shadow: 0 10px 28px rgba(0, 0, 0, 0.1);
  font-family: 'Poppins', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  color: #2f3e4e;
}

.form-title {
  font-weight: 800;
  font-size: 2.2rem;
  letter-spacing: 0.05em;
  color: #1c2833;
  border-bottom: 3px solid #5a9df9;
  padding-bottom: 0.6rem;
  margin-bottom: 2rem;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem 2rem;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group.full-width {
  grid-column: 1 / -1;
}

label {
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #4b5c72;
  font-size: 1rem;
  user-select: none;
}

input[type="number"],
input[type="date"],
select,
textarea {
  font-size: 1rem;
  padding: 0.6rem 1rem;
  border-radius: 14px;
  border: 2px solid #cbd3dc;
  transition: all 0.3s ease;
  background: #f9fbfd;
  font-family: inherit;
  resize: vertical;
  box-shadow: inset 2px 2px 5px #e1e7f0,
              inset -2px -2px 5px #ffffff;
}

input[type="number"]:focus,
input[type="date"]:focus,
select:focus,
textarea:focus {
  outline: none;
  border-color: #5a9df9;
  background: #e8f0fe;
  box-shadow: 0 0 8px #5a9df9;
}

textarea {
  min-height: 80px;
}

.btn-submit {
  grid-column: 1 / -1;
  padding: 0.85rem 0;
  font-size: 1.25rem;
  font-weight: 700;
  color: white;
  background: linear-gradient(135deg, #4f8ef7 0%, #1f65e8 100%);
  border: none;
  border-radius: 20px;
  cursor: pointer;
  box-shadow: 0 6px 15px rgba(31, 101, 232, 0.6);
  user-select: none;
  transition: background 0.35s ease, box-shadow 0.35s ease;
  margin-top: 1.25rem;
}

.btn-submit:hover,
.btn-submit:focus {
  background: linear-gradient(135deg, #1f65e8 0%, #4f8ef7 100%);
  box-shadow: 0 10px 24px rgba(31, 101, 232, 0.8);
  outline: none;
}
</style>
