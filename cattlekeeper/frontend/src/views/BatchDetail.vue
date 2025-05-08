<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter} from 'vue-router';
import api from '@/api/axios';

const route = useRoute();
const batch = ref(null);
const error = ref(null);
const router = useRouter();

onMounted(async () => {
  const slug = route.params.batch_slug;
  try {
    const response = await api.get(`api/farm/batch/${slug}/`);
    batch.value = response.data;
  } catch (err) {
    error.value = 'No se pudo cargar el lote.';
    console.error(err);
  }
});
const goToUpdate = () => {
  const batchSlug = route.params.batch_slug;
  router.push({ name: 'BatchUpdate', params: { batch_slug: batchSlug } });
};
</script>

<template>
  <div>
    <h1>Detalle del Lote</h1>
    <div v-if="error">
      <p style="color: red">{{ error }}</p>
    </div>
    <div v-else-if="batch">
      <p><strong>Nombre:</strong> {{ batch.name }}</p>
      <p><strong>Especie:</strong> {{ batch.species }}</p>
      <p><strong>Sexo:</strong> {{ batch.sex }}</p>
      <p><strong>Cantidad:</strong> {{ batch.quantity }}</p>
      <p><strong>Origen:</strong> {{ batch.origin }}</p>
      <p><strong>Notas:</strong> {{ batch.notes }}</p>
      <p><strong>Fecha de compra:</strong> {{ batch.purchase_date }}</p>
      <button @click="goToUpdate">Actualizar Lote</button>
      <button @click="$router.push({ name: 'BatchAnimalList', params: { batch_slug: batch.slug } })">
      Ver animales
    </button>
    <router-link :to="`/batch/${batch.slug}/delete`">
      <button>Eliminar Lote</button>
    </router-link>


    </div>
    <div v-else>
      <p>Cargando lote...</p>
    </div>
  </div>
</template>
