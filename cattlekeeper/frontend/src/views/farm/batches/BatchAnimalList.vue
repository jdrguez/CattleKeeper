<template>
    <div>
      <h2>Animales del lote</h2>
      <ul>
        <li v-for="animal in animals" :key="animal.slug">
          {{ animal.identifier }} - {{ animal.weight }} kg
          <button @click="$router.push({ name: 'AnimalDetail', params: { batch_slug: animal.batch, animal_slug: animal.slug } })">
            Ver detalle
            </button>
            <button @click="$router.push({ name: 'AnimalUpdate', params: { batch_slug: animal.batch, animal_slug: animal.slug } })">
            Editar Animal
            </button>
        </li>
        <li>
            <button @click="$router.push({ name: 'AnimalCreate', params: { batch_slug: slug } })">
            Añadir animal
            </button>
        </li>
      </ul>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useRoute } from 'vue-router'
  import api from '@/api/axios'
  
  const route = useRoute()
  const animals = ref([])
  
  onMounted(async () => {
    const slug = route.params.batch_slug
    const response = await api.get(`/api/farm/batch/${slug}/animals/`)
    animals.value = response.data
  })
  </script>
  