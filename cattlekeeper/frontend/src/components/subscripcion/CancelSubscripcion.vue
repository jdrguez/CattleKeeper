<template>
    <div class="card shadow-sm mx-auto my-5" style="max-width: 500px;">
      <div class="card-body">
        <h5 class="card-title">Cancel Subscription</h5>
  
        <div v-if="loading" class="text-muted mb-3">
          Processing...
        </div>
  
        <div v-else>
          <p class="card-text">Are you sure you want to cancel your subscription?</p>
  
          <button
            class="btn btn-danger"
            @click="cancelSubscription"
            :disabled="isSubmitting"
          >
            Cancel Subscription
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
      message.value = response.data.message || 'Subscription cancelled successfully.'
    } catch (err) {
      if (err.response && err.response.data && err.response.data.error) {
        error.value = err.response.data.error
      } else {
        error.value = 'Network or server error.'
      }
    } finally {
      loading.value = false
      isSubmitting.value = false
    }
  }
  </script>
  
  <style scoped>
  </style>