<template>
    <div>
      <h1>Eliminar Lote</h1>
      <p v-if="batch">¿Estás seguro de que deseas eliminar el lote "{{ batch.name }}"?</p>
      <p v-else>Cargando datos del lote...</p>
      <div v-if="error" class="error">{{ error }}</div>
      <button @click="deleteBatch">Eliminar</button>
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
  const batch = ref(null)
  const error = ref('')
  
  onMounted(async () => {
    try {
      const response = await api.get(`/api/farm/batch/${batchSlug}/`)
      batch.value = response.data
    } catch (err) {
      error.value = 'Error al cargar los datos del lote'
    }
  })
  
  const deleteBatch = async () => {
    try {
      await api.delete(`/api/farm/batch/${batchSlug}/delete/`)
      router.push({ name: 'batch-list', params: { batch_slug: batchSlug } })
    } catch (err) {
      error.value = 'Error al eliminar el lote'
    }
  }
  
  const cancel = () => {
    router.go(-1)
  }
  </script>