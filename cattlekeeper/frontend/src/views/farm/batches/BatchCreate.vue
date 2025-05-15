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
  <div class="container mt-5">
    <div class="card shadow-sm">
      <div class="card-header bg-success text-white">
        <h2 class="mb-0">Crear nuevo lote</h2>
      </div>
      <div class="card-body">
        <form @submit.prevent="createBatch">
          <div class="row g-3">

            <div class="col-md-6">
              <label class="form-label">Especie <span class="text-danger">*</span></label>
              <select v-model="form.species" class="form-select" required>
                <option value="" disabled>Seleccionar especie...</option>
                <option
                  v-for="option in speciesOptions"
                  :key="option.value"
                  :value="option.value"
                >
                  {{ option.label }}
                </option>
              </select>
            </div>

            <div class="col-md-6">
              <label class="form-label">Fecha de compra <span class="text-danger">*</span></label>
              <input
                type="date"
                v-model="form.purchase_date"
                class="form-control"
                required
              />
            </div>

            <div class="col-md-4">
              <label class="form-label">Cantidad <span class="text-danger">*</span></label>
              <input
                type="number"
                v-model="form.quantity"
                class="form-control"
                min="1"
                required
              />
            </div>

            <div class="col-md-4">
              <label class="form-label">Sexo</label>
              <select v-model="form.sex" class="form-select">
                <option
                  v-for="option in sexOptions"
                  :key="option.value"
                  :value="option.value"
                >
                  {{ option.label }}
                </option>
              </select>
            </div>

            <div class="col-md-4">
              <label class="form-label">Origen</label>
              <input
                type="text"
                v-model="form.origin"
                class="form-control"
                placeholder="Opcional"
              />
            </div>

            <div class="col-12">
              <label class="form-label">Notas</label>
              <textarea
                v-model="form.notes"
                class="form-control"
                rows="4"
                placeholder="Agregar detalles adicionales..."
              ></textarea>
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
              Crear Lote
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
