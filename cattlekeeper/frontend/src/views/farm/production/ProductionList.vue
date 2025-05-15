<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import api from '@/api/axios';

const route = useRoute();
const router = useRouter(); // Usamos useRouter para navegar
const productions = ref([]);
const batchSlug = route.params.batch_slug;

onMounted(async () => {
  try {
    const response = await api.get(`api/farm/batch/${batchSlug}/production/`);
    productions.value = response.data;
  } catch (error) {
    console.error('Error fetching productions:', error);
  }
});

const goToEdit = (id) => {
  // Usamos router.push para navegar
  router.push({ name: 'ProductionEdit', params: { batch_slug: batchSlug, production_pk: id } });
};

const deleteProduction = async (id) => {
  try {
    await api.post(`api/farm/batch/${batchSlug}/production/${id}/delete/`);
    productions.value = productions.value.filter(p => p.id !== id);
  } catch (error) {
    console.error('Error eliminando producción:', error);
  }
};
</script>

<template>
  <router-link :to="{ name: 'ProductionCreate', params: { batch_slug: batchSlug } }">
    <button>Crear producción</button>
  </router-link>

  <div>
    <h1>Producciones del lote: {{ batchSlug }}</h1>
    <ul v-if="productions.length">
      <li v-for="prod in productions" :key="prod.id">
        <strong>{{ prod.production_type }}</strong>:
        {{ prod.quantity }} {{ prod.unit }}
        ({{ prod.date }})
        <button @click="goToEdit(prod.id)">Editar</button>
        <button @click="deleteProduction(prod.id)">Eliminar</button>
        <div v-if="prod.notes">📝 {{ prod.notes }}</div>
      </li>
    </ul>
    <p v-else>No hay producciones registradas para este lote.</p>
  </div>
</template>
