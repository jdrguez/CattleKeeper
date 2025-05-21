<template>
  <div class="container py-5" style="max-width: 480px;">
    <h2 class="mb-4 border-bottom pb-2 text-center">Create New Animal</h2>

    <form @submit.prevent="createAnimal" class="bg-white p-4 rounded-4 shadow-sm">
      <div class="mb-3">
        <label class="form-label fw-semibold" for="birth_date"><i class="bi bi-calendar"></i> Birth date</label>
        <input
          id="birth_date"
          type="date"
          v-model="form.birth_date"
          required
          class="form-control rounded-pill border-primary"
          style="box-shadow: inset 0 1px 3px rgb(0 0 0 / 0.1);"
        />
      </div>

      <div class="mb-3">
        <label class="form-label fw-semibold" for="weight"><i class="bi bi-speedometer2"></i> Weight (kg)</label>
        <input
          id="weight"
          type="number"
          v-model="form.weight"
          required
          min="0"
          step="0.1"
          class="form-control rounded-pill border-primary"
          placeholder="Ex: 150.5"
          style="box-shadow: inset 0 1px 3px rgb(0 0 0 / 0.1);"
        />
      </div>

      <div class="mb-3">
        <label class="form-label fw-semibold" for="health_status"><i class="bi bi-heart-pulse"></i> Health</label>
        <select
          id="health_status"
          v-model="form.health_status"
          class="form-select rounded-pill border-primary"
          style="box-shadow: inset 0 1px 3px rgb(0 0 0 / 0.1);"
        >
          <option :value="1">Healthy</option>
          <option :value="2">Sick</option>
        </select>
      </div>

      <div class="mb-4">
        <label class="form-label fw-semibold" for="notes"><i class="bi bi-pencil"></i> Notes</label>
        <textarea
          id="notes"
          v-model="form.notes"
          rows="3"
          class="form-control rounded-3 border-secondary"
          placeholder="Additional details..."
          style="resize: vertical;"
        ></textarea>
      </div>

      <button
        type="submit"
        class="btn btn-primary w-100 rounded-pill shadow-sm fw-bold"
        :disabled="!form.birth_date || !form.weight"
      >
        Create Animal
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '@/api/axios'
import { useToast } from 'vue-toastification';

const toast = useToast()
const route = useRoute()
const router = useRouter()

const form = ref({
  birth_date: '',
  weight: '',
  health_status: 1,
  notes: ''
})

const createAnimal = async () => {
  const batchSlug = route.params.batch_slug
  try {
    await api.post(`/api/farm/batch/${batchSlug}/animals/create/`, form.value)
    router.push({ name: 'BatchAnimalList', params: { batch_slug: batchSlug } })
    toast.success('The animal has been created successfully.')
  } catch (error) {
    toast.error('The animal could not be created.')
    console.error(error)
  }
}
</script>
