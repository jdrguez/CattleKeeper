<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import api from '@/api/axios';

const batches = ref([]);
const router = useRouter();

onMounted(async () => {
  try {
    const response = await api.get('api/farm/batch/');
    batches.value = response.data;
  } catch (error) {
    console.error('Error fetching batches:', error);
  }
});

const goToDetail = (slug) => {
  router.push({ name: 'BatchDetail', params: { batch_slug: slug } });
};
</script>

<template>
  <div>
    <h1>Batch List</h1>
    <ul>
      <li v-for="batch in batches" :key="batch.slug">
        {{ batch.name }}
        <button @click="goToDetail(batch.slug)">Ver detalle</button>
      </li>
    </ul>
  </div>
  <router-link to="/batch/create">
    <button>Crear nuevo lote</button>
  </router-link>
</template>
