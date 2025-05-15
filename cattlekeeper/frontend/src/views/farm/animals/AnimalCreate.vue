<template>
    <div>
      <h2>Crear nuevo animal</h2>
      <form @submit.prevent="createAnimal">
        <div>
          <label>Fecha de nacimiento:</label>
          <input type="date" v-model="form.birth_date" required />
        </div>
        <div>
          <label>Peso (kg):</label>
          <input type="number" v-model="form.weight" required />
        </div>
        <div>
          <label>Salud:</label>
          <select v-model="form.health_status">
            <option :value="1">Saludable</option>
            <option :value="2">Enfermo</option>
          </select>
        </div>
        <div>
          <label>Notas:</label>
          <textarea v-model="form.notes" rows="3" />
        </div>
        <button type="submit">Crear Animal</button>
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
    await api.post(`/api/farm/batch/${batchSlug}/animals/create/`, form.value)
    router.push({ name: 'BatchAnimalList', params: { batch_slug: batchSlug } })
  }
  </script>
  