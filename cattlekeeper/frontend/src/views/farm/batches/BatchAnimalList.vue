<template>
  <div class="container py-4">
    <h2 class="mb-4 text-center fw-semibold">Animales del lote</h2>

    <div class="row row-cols-1 row-cols-md-2 g-4">
      <div v-for="animal in animals" :key="animal.slug" class="col">
        <div class="card h-100 shadow-sm border-0 rounded-4 custom-card">
          <div class="card-body">
            <h5 class="card-title mb-2 fw-bold text-primary-emphasis">
              ID: {{ animal.identifier }}
            </h5>
            <p class="card-text mb-3">
              <strong>Peso:</strong> {{ animal.weight }} kg
            </p>
            <div class="d-flex gap-2">
              <button
                class="btn btn-outline-primary btn-sm"
                @click="$router.push({ name: 'AnimalDetail', params: { batch_slug: animal.batch, animal_slug: animal.slug } })"
              >
                Ver detalle
              </button>
              <button
                class="btn btn-outline-secondary btn-sm"
                @click="$router.push({ name: 'AnimalUpdate', params: { batch_slug: animal.batch, animal_slug: animal.slug } })"
              >
                Editar
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Botón Añadir animal -->
    <div class="text-center mt-5">
      <button
        class="btn btn-success btn-lg px-4 rounded-pill shadow"
        @click="$router.push({ name: 'AnimalCreate', params: { batch_slug: route.params.batch_slug } })"
      >
        + Añadir animal
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import api from '@/api/axios'

const route = useRoute()
const animals = ref([])

onMounted(async () => {
  const slug = route.params.batch_slug
  const response = await api.get(`/api/farm/batch/${slug}/animals/`)
  animals.value = response.data
})
</script>

<style scoped>
.custom-card {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  background-color: #f9fafb;
}
.custom-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
}
</style>
