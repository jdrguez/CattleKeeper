<template>
  <div class="container py-5" style="max-width: 480px;">
    <h2 class="mb-4 text-primary border-bottom pb-2">🐄 Crear Nuevo Animal</h2>

    <form @submit.prevent="createAnimal" class="bg-white p-4 rounded-4 shadow-sm">
      <div class="mb-3">
        <label class="form-label fw-semibold" for="birth_date">📅 Fecha de nacimiento</label>
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
        <label class="form-label fw-semibold" for="weight">⚖️ Peso (kg)</label>
        <input
          id="weight"
          type="number"
          v-model="form.weight"
          required
          min="0"
          step="0.1"
          class="form-control rounded-pill border-primary"
          placeholder="Ej: 150.5"
          style="box-shadow: inset 0 1px 3px rgb(0 0 0 / 0.1);"
        />
      </div>

      <div class="mb-3">
        <label class="form-label fw-semibold" for="health_status">🩺 Salud</label>
        <select
          id="health_status"
          v-model="form.health_status"
          class="form-select rounded-pill border-primary"
          style="box-shadow: inset 0 1px 3px rgb(0 0 0 / 0.1);"
        >
          <option :value="1">Saludable</option>
          <option :value="2">Enfermo</option>
        </select>
      </div>

      <div class="mb-4">
        <label class="form-label fw-semibold" for="notes">📝 Notas</label>
        <textarea
          id="notes"
          v-model="form.notes"
          rows="3"
          class="form-control rounded-3 border-secondary"
          placeholder="Detalles adicionales..."
          style="resize: vertical;"
        ></textarea>
      </div>

      <button
        type="submit"
        class="btn btn-primary w-100 rounded-pill shadow-sm fw-bold"
        :disabled="!form.birth_date || !form.weight"
      >
        Crear Animal
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '@/api/axios'

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
  } catch (error) {
    alert('Error al crear el animal. Intenta nuevamente.')
    console.error(error)
  }
}
</script>
