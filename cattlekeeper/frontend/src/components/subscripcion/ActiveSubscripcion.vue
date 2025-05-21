<template>
  <div class="card shadow-sm mx-auto my-4" style="max-width: 600px; border-radius: 1rem; background-color: #fff;">
    <div class="card-body px-5 py-4">
      <h2 class="card-title text-center mb-4 fw-bold text-secondary">My Subscription</h2>
      
      <div v-if="subscription" class="text-dark">
        <p><strong>Plan:</strong> {{ subscription.plan.name }}</p>
        <p><strong>Valid from:</strong> {{ formatDate(subscription.start_date) }}</p>
        <p><strong>Valid until:</strong> {{ formatDate(subscription.end_date) }}</p>
        <p><strong>Active?:</strong> <span :class="subscription.is_active ? 'text-success' : 'text-danger'">{{ subscription.is_active ? 'Yes' : 'No' }}</span></p>
      </div>
      
      <p v-else class="text-muted fst-italic text-center">You don't have any active subscriptions.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api/axios'

const subscription = ref(null)

function formatDate(date) {
  return new Date(date).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  })
}

onMounted(async () => {
  try {
    const response = await api.get('/api/subscription/')
    subscription.value = response.data
  } catch (error) {
    if (error.response && error.response.status === 404) {
      subscription.value = null
    } else {
      console.error('Error getting subscription:', error)
    }
  }
})
</script>
