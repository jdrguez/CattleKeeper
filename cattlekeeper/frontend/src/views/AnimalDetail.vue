<template>
    <div v-if="animal">
      <h2>Detalle del animal</h2>
      <p><strong>Identificador:</strong> {{ animal.identifier }}</p>
      <p><strong>Peso:</strong> {{ animal.weight }} kg</p>
      <p><strong>Fecha de nacimiento:</strong> {{ animal.birth_date }}</p>
      <p><strong>Salud:</strong> {{ animal.health_status }}</p>
      <p><strong>Notas:</strong> {{ animal.notes }}</p>
    </div>
  <button @click="$router.push({ name: 'AnimalDelete', params: { batch_slug: batch_slug, animal_slug: animal_slug } })">
    Eliminar Animal
  </button>

  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useRoute } from 'vue-router'
  import api from '@/api/axios'
  
  const route = useRoute()
  const animal = ref(null)
  
  onMounted(async () => {
    const { batch_slug, animal_slug } = route.params
    const response = await api.get(`/api/farm/batch/${batch_slug}/animals/${animal_slug}/`)
    animal.value = response.data
  })
  </script>
  