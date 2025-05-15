<template>
    <div>
      <h1>Eliminar Animal</h1>
      <p v-if="animal">¿Estás seguro de que deseas eliminar al animal "{{ animal.identifier }}"?</p>
      <p v-else>Cargando datos del animal...</p>
      <div v-if="error" class="error">{{ error }}</div>
      <button @click="deleteAnimal">Eliminar</button>
      <button @click="cancel">Cancelar</button>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import api from '@/api/axios'
  
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
      error.value = 'Error al cargar los datos del animal'
    }
  })
  
  const deleteAnimal = async () => {
    try {
      await api.delete(`/api/farm/batch/${batchSlug}/animals/${animalSlug}/delete/`)
      router.push({ name: 'BatchAnimalList', params: { batch_slug: batchSlug } })
    } catch (err) {
      error.value = 'Error al eliminar el animal'
    }
  }
  
  const cancel = () => {
    router.go(-1)
  }
  </script>
  