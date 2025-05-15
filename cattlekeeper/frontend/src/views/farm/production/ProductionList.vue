<template>
  <div class="production-container mx-auto p-4" style="max-width: 720px;">
    <div class="header d-flex justify-content-between align-items-center mb-4">
      <h1 class="title mb-0">Producciones del lote: <span class="text-secondary">{{ batchSlug }}</span></h1>
      <router-link :to="{ name: 'ProductionCreate', params: { batch_slug: batchSlug } }" class="btn-create">
        + Crear producción
      </router-link>
    </div>

    <ul v-if="productions.length" class="production-list">
      <li v-for="prod in productions" :key="prod.id" class="production-item shadow-sm rounded">
        <div class="production-info">
          <strong class="production-type">{{ prod.production_type }}</strong>
          <span class="production-qty">{{ prod.quantity }} {{ prod.unit }}</span>
          <span class="production-date">{{ prod.date }}</span>
        </div>

        <div v-if="prod.notes" class="production-notes">📝 {{ prod.notes }}</div>

        <div class="actions">
          <button @click="goToEdit(prod.id)" class="btn-edit">Editar</button>
          <button @click="deleteProduction(prod.id)" class="btn-delete">Eliminar</button>
        </div>
      </li>
    </ul>

    <p v-else class="no-data">No hay producciones registradas para este lote.</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import api from '@/api/axios';

const route = useRoute();
const router = useRouter();
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

<style scoped>
.production-container {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: #fff;
  border-radius: 14px;
  padding: 1.5rem 2rem;
  box-shadow: 0 6px 15px rgba(0,0,0,0.08);
  color: #333;
}

.header {
  border-bottom: 2px solid #eee;
  padding-bottom: 0.75rem;
}

.title {
  font-weight: 700;
  font-size: 1.8rem;
}

.text-secondary {
  color: #6c757d;
  font-weight: 500;
}

.btn-create {
  background-color: #28a745;
  color: white;
  font-weight: 600;
  padding: 0.4rem 1.1rem;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(40, 167, 69, 0.35);
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
  text-decoration: none;
  user-select: none;
}

.btn-create:hover,
.btn-create:focus {
  background-color: #218838;
  box-shadow: 0 6px 14px rgba(33, 136, 56, 0.5);
  outline: none;
}

.production-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.production-item {
  background: #f9fafb;
  margin-bottom: 1rem;
  padding: 1rem 1.2rem;
  display: flex;
  flex-direction: column;
  border-radius: 12px;
  transition: box-shadow 0.3s ease;
}

.production-item:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.08);
}

.production-info {
  display: flex;
  gap: 1.2rem;
  font-size: 1.05rem;
  margin-bottom: 0.4rem;
  flex-wrap: wrap;
  color: #2c3e50;
}

.production-type {
  font-weight: 700;
  color: #007bff;
}

.production-qty,
.production-date {
  color: #495057;
}

.production-notes {
  font-style: italic;
  font-size: 0.9rem;
  color: #6c757d;
  margin-bottom: 0.8rem;
}

.actions {
  margin-top: auto;
  display: flex;
  gap: 0.8rem;
}

button {
  border: none;
  cursor: pointer;
  font-weight: 600;
  border-radius: 10px;
  padding: 0.4rem 1rem;
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
  user-select: none;
}

.btn-edit {
  background-color: #17a2b8;
  color: white;
  box-shadow: 0 4px 10px rgba(23, 162, 184, 0.35);
}

.btn-edit:hover,
.btn-edit:focus {
  background-color: #138496;
  box-shadow: 0 6px 14px rgba(19, 132, 150, 0.5);
  outline: none;
}

.btn-delete {
  background-color: #dc3545;
  color: white;
  box-shadow: 0 4px 10px rgba(220, 53, 69, 0.35);
}

.btn-delete:hover,
.btn-delete:focus {
  background-color: #c82333;
  box-shadow: 0 6px 14px rgba(200, 35, 51, 0.5);
  outline: none;
}

.no-data {
  text-align: center;
  color: #868e96;
  font-style: italic;
  margin-top: 2rem;
  font-size: 1.1rem;
}
</style>
