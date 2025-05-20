<template>
  <div class="container py-5">
    <h1 class="text-center mb-5 text-success fw-bold display-5">Planes de Suscripción</h1>

    <div class="row g-4">
      <div class="col-12 col-sm-6 col-lg-4" v-for="plan in plans" :key="plan.id">
        <div class="card h-100 shadow-sm border-success">
          <div class="card-body">
            <h5 class="card-title text-success">{{ plan.name }}</h5>
            <p class="card-text mb-1"><strong>💶 Precio:</strong> €{{ plan.price }}</p>
            <p class="card-text"><strong>📅 Duración:</strong> {{ plan.duration_days }} días</p>
          </div>
          <div class="card-footer bg-transparent border-top-0">
            <RouterLink
              :to="`/plans/subscribe/${plan.id}`"
              class="btn btn-success w-100"
            >
              ✅ Elegir este plan
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import api from '@/api/axios'

const plans = ref([])

onMounted(async () => {
  try {
    const response = await api.get('/api/subscription/plans')
    plans.value = response.data
  } catch (error) {
    console.error('Error al obtener los planes:', error)
  }
})
</script>
