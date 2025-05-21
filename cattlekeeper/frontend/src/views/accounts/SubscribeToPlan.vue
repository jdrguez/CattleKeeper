<template>
  <div class="page-container">
    <h1 class="page-title">Confirm Subscription</h1>
    
    <div class="form-content">
      <div v-if="plan" class="plan-card">
        <h2 class="plan-name">{{ plan.name }}</h2>
        
        <div class="plan-details">
          <div class="plan-detail-item">
            <span class="detail-label">Price:</span>
            <span class="detail-value">€{{ plan.price }}</span>
          </div>
          <div class="plan-detail-item">
            <span class="detail-label">Duration:</span>
            <span class="detail-value">{{ plan.duration_days }} days</span>
          </div>
        </div>

        <div class="form-actions">
          <button 
            @click="subscribe" 
            class="btn btn-success"
          >
            Confirm Subscription
          </button>
        </div>
      </div>

      <div v-if="message" class="alert-message" :class="message.includes('Error') ? 'error' : 'success'">
        {{ message }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '@/api/axios'
import { useSubscriptionStore } from '@/stores/subscription'

const route = useRoute()
const router = useRouter()
const subscription = useSubscriptionStore()
const planId = route.params.planId

const plan = ref(null)
const message = ref('')

onMounted(async () => {
  try {
    const response = await api.get(`/api/subscription/plans/${planId}`)
    plan.value = response.data
  } catch (error) {
    console.error('Error loading plan:', error)
    message.value = 'Plan not found.'
  }
})

const subscribe = async () => {
  try {
    const response = await api.post('/api/subscription/create/', {
      plan_id: plan.value.id
    })
    await subscription.checkSubscription()
    message.value = response.data.message || 'Subscription created successfully.'
  } catch (error) {
    message.value = error.response?.data?.error || 'Error subscribing to plan.'
  }
}
</script>

<style scoped>
.page-container {
  margin: 2rem auto;
  background: #fff;
  padding: 2rem 2.5rem;
  border-radius: 14px;
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #2d3a45;
  max-width: 600px;
}

.page-title {
  font-size: 2.1rem;
  font-weight: 700;
  border-bottom: 3px solid #28a745;
  padding-bottom: 0.3rem;
  margin-bottom: 1.8rem;
  letter-spacing: 0.03em;
}

.form-content {
  background: #f6f9fc;
  padding: 2rem;
  border-radius: 14px;
  box-shadow: inset 2px 2px 6px #d9e6f0, inset -2px -2px 6px #ffffff;
}

.plan-card {
  padding: 1.5rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

.plan-name {
  font-size: 1.5rem;
  font-weight: 600;
  color: #2d3a45;
  margin-bottom: 1.5rem;
  text-align: center;
}

.plan-details {
  margin-bottom: 2rem;
}

.plan-detail-item {
  display: flex;
  justify-content: space-between;
  padding: 1rem 0;
  border-bottom: 1px solid #e9ecef;
}

.detail-label {
  font-weight: 600;
  color: #4a5568;
}

.detail-value {
  color: #2d3a45;
}

.form-actions {
  display: flex;
  justify-content: center;
  padding-top: 1.5rem;
}

.btn {
  padding: 0.55rem 1.6rem;
  font-weight: 700;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-success {
  background: linear-gradient(135deg, #28a745, #1e7e34);
  color: white;
  box-shadow: 0 6px 16px rgba(30, 126, 52, 0.5);
}

.btn-success:hover {
  background: linear-gradient(135deg, #1e7e34, #28a745);
  box-shadow: 0 8px 24px rgba(30, 126, 52, 0.8);
}

.alert-message {
  padding: 1rem;
  border-radius: 12px;
  margin-top: 1.5rem;
  font-weight: 600;
}

.alert-message.success {
  background-color: #d4edda;
  color: #155724;
}

.alert-message.error {
  background-color: #f8d7da;
  color: #721c24;
}
</style>