<template>
  <div class="delete-animal-container p-4 mx-auto" style="max-width: 460px;">
    <h1 class="mb-3 text-danger border-bottom pb-2">🗑️ Eliminar Animal</h1>

    <p v-if="animal" class="lead">
      ¿Estás seguro de que deseas eliminar al animal
      <strong class="text-primary">"{{ animal.identifier }}"</strong>?
    </p>

    <p v-else class="text-muted">Cargando datos del animal...</p>

    <div v-if="error" class="alert alert-warning mt-3">
      {{ error }}
    </div>

    <div class="d-flex gap-3 mt-4">
      <button
        class="btn btn-danger flex-grow-1 fw-semibold shadow-sm"
        @click="deleteAnimal"
        :disabled="!animal"
        aria-label="Confirmar eliminación de animal"
      >
        Eliminar
      </button>

      <button
        class="btn btn-outline-secondary flex-grow-1 fw-semibold shadow-sm"
        @click="cancel"
        aria-label="Cancelar eliminación y volver"
      >
        Cancelar
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '@/api/axios'

const route = useRoute()
const router = useRouter()

const batchSlug = route.params.batch_slug
const animalSlug = route.params.animal_slug

const animal = ref(null)
const error = ref('')

onMounted(async () => {
  try {
    const response = await api.get(`/api/farm/batch/${batchSlug}/animals/${animalSlug}/`)
    animal.value = response.data
  } catch (err) {
    error.value = 'Error al cargar los datos del animal'
  }
})

const deleteAnimal = async () => {
  try {
    await api.delete(`/api/farm/batch/${batchSlug}/animals/${animalSlug}/delete/`)
    router.push({ name: 'BatchAnimalList', params: { batch_slug: batchSlug } })
  } catch (err) {
    error.value = 'Error al eliminar el animal'
  }
}

const cancel = () => {
  router.go(-1)
}
</script>

<style scoped>
.delete-animal-container {
  background: #fff;
  border-radius: 16px;
  box-shadow:
    0 6px 10px rgba(0, 0, 0, 0.1),
    0 1px 3px rgba(0, 0, 0, 0.06);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h1 {
  font-weight: 700;
}

.lead {
  font-size: 1.125rem;
}

button:disabled {
  cursor: not-allowed;
  opacity: 0.6;
  box-shadow: none !important;
}
</style>
