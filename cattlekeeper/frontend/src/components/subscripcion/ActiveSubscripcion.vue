<template>
    <div>
      <h2>Mi suscripción</h2>
      <div v-if="subscription">
        <p><strong>Plan:</strong> {{ subscription.plan.name }}</p>
        <p><strong>Válido desde:</strong> {{ subscription.start_date }}</p>
        <p><strong>Válido hasta:</strong> {{ subscription.end_date }}</p>
        <p><strong>¿Activa?:</strong> {{ subscription.is_active ? 'Sí' : 'No' }}</p>
      </div>
      <p v-else>No tienes ninguna suscripción activa.</p>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import api from '@/api/axios'  
  const subscription = ref(null)
  
  onMounted(async () => {
    try {
      const response = await api.get('/api/subscription/')
      subscription.value = response.data
    } catch (error) {
      if (error.response && error.response.status === 404) {
        subscription.value = null
      } else {
        console.error('Error al obtener la suscripción:', error)
      }
    }
  })
  </script>
  