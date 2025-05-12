<template>
  <div>
    <h2>Crear Evento de Salud</h2>
    <form @submit.prevent="submitEvent">
      <div>
        <label>Fecha:</label>
        <input type="date" v-model="form.date" required />
      </div>

      <div>
        <label>Tipo de Evento:</label>
        <select v-model="form.event_type" required>
          <option disabled value="">Selecciona tipo</option>
          <option value="VACCINE">Vacuna</option>
          <option value="ILLNESS">Enfermedad</option>
          <option value="CHECKUP">Chequeo</option>
          <option value="SURGERY">Cirugía</option>
        </select>
      </div>

      <div>
        <label>Descripción:</label>
        <textarea v-model="form.description" required></textarea>
      </div>

      <div>
        <label>Veterinario (opcional):</label>
        <input type="text" v-model="form.veterinarian" />
      </div>

      <button type="submit">Guardar</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '@/api/axios'

const route = useRoute()
const router = useRouter()
const { batch_slug, animal_slug } = route.params

const form = ref({
  date: '',
  event_type: '',
  description: '',
  veterinarian: ''
})

const submitEvent = async () => {
  await api.post(`/api/farm/batch/${batch_slug}/animals/${animal_slug}/health/create/`, form.value)
  router.push({ name: 'AnimalDetail', params: { batch_slug, animal_slug } })
}
</script>
