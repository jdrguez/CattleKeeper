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
  const res = await api.get(`/api/farm/batch/${batch_slug}/animals/${animal_slug}/`)
  animal.value = res.data
})

const updateAnimal = async () => {
  const { batch_slug, animal_slug } = route.params
  await api.post(`/api/farm/batch/${batch_slug}/animals/${animal_slug}/update/`, animal.value)
  alert('Animal actualizado')
  router.back()
}
</script>

<template>
  <form @submit.prevent="updateAnimal">
    <label>Fecha de nacimiento:</label>
    <input type="date" v-model="animal.birth_date" />

    <label>Peso:</label>
    <input type="number" v-model="animal.weight" />

    <label>Estado de salud:</label>
    <select v-model="animal.health_status">
      <option :value="1">Saludable</option>
      <option :value="2">Enfermo</option>
      <option :value="3">Muerto</option>
    </select>

    <label>Notas:</label>
    <textarea v-model="animal.notes" />

    <button type="submit">Actualizar Animal</button>
  </form>
</template>
