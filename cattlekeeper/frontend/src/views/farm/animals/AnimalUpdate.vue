<template>
  <div class="container py-5" style="max-width: 480px;">
    <h2 class="mb-4 text-primary border-bottom pb-2">✏️ Editar Animal</h2>

    <form @submit.prevent="updateAnimal" class="bg-white p-4 rounded-4 shadow-sm">
      <div class="mb-4">
        <label for="birth_date" class="form-label fw-semibold">📅 Fecha de nacimiento</label>
        <input
          id="birth_date"
          type="date"
          v-model="animal.birth_date"
          class="form-control rounded-pill border-primary"
          style="box-shadow: inset 0 1px 3px rgb(0 0 0 / 0.1);"
        />
      </div>

      <div class="mb-4">
        <label for="weight" class="form-label fw-semibold">⚖️ Peso (kg)</label>
        <input
          id="weight"
          type="number"
          v-model="animal.weight"
          min="0"
          step="0.1"
          class="form-control rounded-pill border-primary"
          placeholder="Ej: 150.5"
          style="box-shadow: inset 0 1px 3px rgb(0 0 0 / 0.1);"
        />
      </div>

      <div class="mb-4">
        <label for="health_status" class="form-label fw-semibold">🩺 Estado de salud</label>
        <select
          id="health_status"
          v-model="animal.health_status"
          class="form-select rounded-pill border-primary"
          style="box-shadow: inset 0 1px 3px rgb(0 0 0 / 0.1);"
        >
          <option :value="1">Saludable</option>
          <option :value="2">Enfermo</option>
          <option :value="3">Muerto</option>
        </select>
      </div>

      <div class="mb-4">
        <label for="notes" class="form-label fw-semibold">📝 Notas</label>
        <textarea
          id="notes"
          v-model="animal.notes"
          rows="4"
          class="form-control rounded-3 border-secondary"
          placeholder="Detalles adicionales..."
          style="resize: vertical;"
        ></textarea>
      </div>

      <button
        type="submit"
        class="btn btn-primary w-100 rounded-pill shadow-sm fw-bold"
      >
        Actualizar Animal
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '@/api/axios'

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
    animal.value = res.data
  } catch (error) {
    console.error('Error al cargar animal:', error)
  }
})

const updateAnimal = async () => {
  const { batch_slug, animal_slug } = route.params
  try {
    await api.post(`/api/farm/batch/${batch_slug}/animals/${animal_slug}/update/`, animal.value)
    alert('Animal actualizado')
    router.back()
  } catch (error) {
    alert('Error al actualizar el animal')
    console.error(error)
  }
}
</script>
