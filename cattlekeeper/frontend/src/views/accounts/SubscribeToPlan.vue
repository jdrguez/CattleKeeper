
<template>
    <div class="p-6 max-w-xl mx-auto">
      <h1 class="text-2xl font-bold mb-4">Confirmar suscripción</h1>
      <div v-if="plan" class="border rounded-xl p-4 shadow">
        <h2 class="text-xl font-semibold">{{ plan.name }}</h2>
        <p class="text-gray-600 mt-2">Precio: €{{ plan.price }}</p>
        <p class="text-gray-600">Duración: {{ plan.duration_days }} días</p>
        <button
          @click="subscribe"
          class="mt-4 bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
        >
          Confirmar suscripción
        </button>
      </div>
      <p v-if="message" class="mt-4 text-green-700">{{ message }}</p>
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
  
  console.log(planId)
  
  const plan = ref(null)
  const message = ref('')
  
  onMounted(async () => {
  try {
    const response = await api.get(`/api/subscription/plans/${planId}`)
    plan.value = response.data
  } catch (error) {
    console.error('Error al cargar el plan:', error)
    message.value = 'Plan no encontrado.'
  }
})

  
  const subscribe = async () => {
    try {
      const response = await api.post('/api/subscription/create/', {
        plan_id: plan.value.id
      })
      await subscription.checkSubscription()
      message.value = response.data.message || 'Suscripción creada.'
    } catch (error) {
      message.value = error.response?.data?.error || 'Error al suscribirse.'
    }
  }
  </script>
  