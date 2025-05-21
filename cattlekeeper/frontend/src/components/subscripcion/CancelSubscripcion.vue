<template>
    <div class="card shadow-sm mx-auto my-5" style="max-width: 500px;">
      <div class="card-body">
        <h5 class="card-title">Cancelar suscripción</h5>
  
        <div v-if="loading" class="text-muted mb-3">
          Procesando...
        </div>
  
        <div v-else>
          <p class="card-text">¿Estás seguro de que deseas cancelar tu suscripción?</p>
  
          <button
            class="btn btn-danger"
            @click="cancelSubscription"
            :disabled="isSubmitting"
          >
            Cancelar suscripción
          </button>
  
          <div v-if="message" class="alert alert-success mt-3" role="alert">
            {{ message }}
          </div>
          <div v-if="error" class="alert alert-danger mt-3" role="alert">
            {{ error }}
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import api from '@/api/axios'  
  
  const loading = ref(false)
  const isSubmitting = ref(false)
  const message = ref('')
  const error = ref('')
  
  const cancelSubscription = async () => {
    loading.value = true
    isSubmitting.value = true
    message.value = ''
    error.value = ''
  
    try {
      const response = await api.post('/api/subscription/cancel/')
      message.value = response.data.message || 'Suscripción cancelada correctamente.'
    } catch (err) {
      if (err.response && err.response.data && err.response.data.error) {
        error.value = err.response.data.error
      } else {
        error.value = 'Error de red o del servidor.'
      }
    } finally {
      loading.value = false
      isSubmitting.value = false
    }
  }
  </script>
  
  <style scoped>
  </style>
  