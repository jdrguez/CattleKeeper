<template>
  <div class="delete-animal-container p-5 mx-auto bg-white rounded-4 shadow-sm" style="max-width: 480px;">
    <div class="text-center mb-4">
      <i class="bi bi-exclamation-triangle-fill text-danger" style="font-size: 2.5rem;"></i>
      <h1 class="mt-3 text-danger fw-light">Delete Animal</h1>
    </div>

    <div class="text-center px-3">
      <p v-if="animal" class="fs-5 text-muted">
        Are you sure you want to permanently delete<br>
        <span class="text-dark fw-medium">"{{ animal.identifier }}"</span>?
      </p>

      <p v-else class="text-muted">Loading animal data...</p>

      <div v-if="error" class="alert alert-warning mt-3 mb-0">
        {{ error }}
      </div>
    </div>

    <div class="d-flex gap-3 mt-5 pt-3">
      <button
        class="btn btn-light flex-grow-1 border shadow-sm py-2"
        @click="cancel"
        aria-label="Cancel deletion and return"
      >
        Cancel
      </button>
      <button
        class="btn btn-danger flex-grow-1 shadow-sm py-2"
        @click="deleteAnimal"
        :disabled="!animal"
        aria-label="Confirm animal deletion"
      >
        Confirm Delete
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '@/api/axios'
import { useToast } from 'vue-toastification';

const toast = useToast()
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
    error.value = 'Error loading animal data'
  }
})

const deleteAnimal = async () => {
  try {
    await api.delete(`/api/farm/batch/${batchSlug}/animals/${animalSlug}/delete/`)
    router.push({ name: 'BatchAnimalList', params: { batch_slug: batchSlug } })
    toast.success('The animal was successfully deleted.')
  } catch (err) {
    error.value = 'Error deleting animal'
    toast.error('Error deleting animal.')
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
