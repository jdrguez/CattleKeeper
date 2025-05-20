<template>
  <div class="card shadow-sm mx-auto my-4" style="max-width: 600px; border-radius: 1rem; background-color: #fff;">
    <div class="card-body px-5 py-4">
      <h2 class="card-title text-center mb-4 fw-bold text-secondary">Mi suscripción</h2>
      
      <div v-if="subscription" class="text-dark">
        <p><strong>Plan:</strong> {{ subscription.plan.name }}</p>
        <p><strong>Válido desde:</strong> {{ subscription.start_date }}</p>
        <p><strong>Válido hasta:</strong> {{ subscription.end_date }}</p>
        <p><strong>¿Activa?:</strong> <span :class="subscription.is_active ? 'text-success' : 'text-danger'">{{ subscription.is_active ? 'Sí' : 'No' }}</span></p>
      </div>
      
      <p v-else class="text-muted fst-italic text-center">No tienes ninguna suscripción activa.</p>
    </div>
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
