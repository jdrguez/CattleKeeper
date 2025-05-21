<template>
  <div class="container py-5" style="max-width: 480px;">
    <h2 class="mb-4 border-bottom pb-2 text-center">
      <i class="bi bi-pencil-square"></i> &nbsp; Edit Animal
    </h2>

    <form @submit.prevent="updateAnimal" class="bg-white p-4 rounded-4 shadow-sm">
      <div class="mb-3">
        <label class="form-label fw-semibold" for="birth_date">
          <i class="bi bi-calendar"></i> Birth date
        </label>
        <input
          id="birth_date"
          type="date"
          v-model="animal.birth_date"
          class="form-control rounded-pill border-primary"
          style="box-shadow: inset 0 1px 3px rgb(0 0 0 / 0.1);"
        />
      </div>

      <div class="mb-3">
        <label class="form-label fw-semibold" for="weight">
          <i class="bi bi-speedometer2"></i> Weight (kg)
        </label>
        <input
          id="weight"
          type="number"
          v-model="animal.weight"
          required
          min="0"
          step="0.1"
          class="form-control rounded-pill border-primary"
          placeholder="Ex: 150.5"
          style="box-shadow: inset 0 1px 3px rgb(0 0 0 / 0.1);"
        />
      </div>

      <div class="mb-3">
        <label class="form-label fw-semibold" for="health_status">
          <i class="bi bi-heart-pulse"></i> Health
        </label>
        <select
          id="health_status"
          v-model.number="animal.health_status"
          class="form-select rounded-pill border-primary"
        >
          <option :value="1">Healthy</option>
          <option :value="2">Sick</option>
          <option :value="3">Recovering</option>
          <option :value="4">Dead</option>
        </select>
      </div>

      <div class="mb-4">
        <label class="form-label fw-semibold" for="notes">
          <i class="bi bi-pencil"></i> Notes
        </label>
        <textarea
          id="notes"
          v-model="animal.notes"
          rows="3"
          class="form-control rounded-3 border-secondary"
          placeholder="Additional details..."
          style="resize: vertical;"
        ></textarea>
      </div>

      <button
        type="submit"
        class="btn btn-primary w-100 rounded-pill shadow-sm fw-bold"
      >
        Update Animal
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '@/api/axios'
import { useToast } from 'vue-toastification'

const toast = useToast()
const route = useRoute()
const router = useRouter()

const animal = ref({
  birth_date: '',
  weight: '',
  health_status: 1,
  notes: ''
})

onMounted(async () => {
  const { batch_slug, animal_slug } = route.params
  try {
    const res = await api.get(`/api/farm/batch/${batch_slug}/animals/${animal_slug}/`)
    const data = res.data
    if (data.birth_date) {
      data.birth_date = data.birth_date.slice(0, 10)
    }
    animal.value = data
  } catch (error) {
    console.error('Error al cargar animal:', error)
  }
})

const updateAnimal = async () => {
  const { batch_slug, animal_slug } = route.params
  const payload = { ...animal.value }

  if (!payload.birth_date) delete payload.birth_date

  try {
    await api.post(`/api/farm/batch/${batch_slug}/animals/${animal_slug}/update/`, payload)
    toast.success('The animal has been updated successfully.')
    router.back()
  } catch (error) {
    toast.error('Error updating animal.')
    console.error(error)
  }
}
</script>
