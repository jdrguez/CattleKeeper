<template>
    <div>
      <h2>Editar Lote</h2>
  
      <form @submit.prevent="updateBatch">
  
        <div>
          <label>Fecha de compra:</label>
          <input type="date" v-model="batch.purchase_date" required />
        </div>
  
        <div>
          <label>Cantidad:</label>
          <input type="number" v-model="batch.quantity" required />
        </div>
  
        <div>
          <label>Origen:</label>
          <input type="text" v-model="batch.origin" />
        </div>
  
        <div>
          <label>Notas:</label>
          <textarea v-model="batch.notes" rows="3" />
        </div>
  
        <button type="submit">Actualizar Lote</button>
      </form>
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
  