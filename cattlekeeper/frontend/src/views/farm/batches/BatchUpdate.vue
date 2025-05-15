<template>
  <div class="container py-5 d-flex justify-content-center">
    <div class="card shadow-sm p-4 rounded-4 w-100" style="max-width: 600px; background-color: #fefefe;">
      <h2 class="text-center mb-4 text-primary-emphasis fw-semibold">Editar Lote</h2>

      <form @submit.prevent="updateBatch" class="d-flex flex-column gap-3">

        <div>
          <label class="form-label">📅 Fecha de compra</label>
          <input type="date" v-model="batch.purchase_date" class="form-control rounded-pill shadow-sm" required />
        </div>
        <div>
          <label class="form-label">🌍 Origen</label>
          <input type="text" v-model="batch.origin" class="form-control rounded-pill shadow-sm" />
        </div>

        <div>
          <label class="form-label">📝 Notas</label>
          <textarea v-model="batch.notes" class="form-control shadow-sm rounded-4" rows="3" />
        </div>

        <div class="d-flex justify-content-center mt-3">
          <button type="submit" class="btn btn-primary px-5 py-2 rounded-pill shadow">
            Guardar cambios
          </button>
        </div>

      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import api from '@/api/axios';

const route = useRoute();
const router = useRouter();

const batch = ref({});

const sexOptions = [
  { value: 1, label: 'Male' },
  { value: 2, label: 'Female' },
  { value: 3, label: 'Mixed' }
];

onMounted(async () => {
  const batchSlug = route.params.batch_slug;
  try {
    const response = await api.get(`/api/farm/batch/${batchSlug}/`);
    batch.value = response.data;
  } catch (error) {
    console.error('Error al cargar el lote para edición:', error);
  }
});

const updateBatch = async () => {
  const batchSlug = route.params.batch_slug;
  const updatedData = {
    purchase_date: batch.value.purchase_date,
    quantity: batch.value.quantity,
    origin: batch.value.origin,
    notes: batch.value.notes
  };

  try {
    await api.post(`/api/farm/batch/${batchSlug}/update/`, updatedData);
    alert('Lote actualizado correctamente');
    router.push({ name: 'batch-list' });
  } catch (error) {
    console.error('Error al actualizar el lote:', error);
    alert('Hubo un error al actualizar el lote.');
  }
};
</script>
