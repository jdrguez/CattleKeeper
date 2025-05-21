<template>
  <div class="container py-5">
    <h1 class="text-center mb-5 fw-bold display-5">Subscription Plans</h1>

    <div class="row justify-content-center mb-5">
      <div class="col-12 col-md-10">
        <div class="alert alert-warning shadow-sm rounded-4 px-4 py-4 text-center">
          <h4 class="mb-3 fw-bold text-success">Why Go Premium?</h4>
          <p class="mb-0 fs-5 text-muted">
            By subscribing you get access to a <strong>personalized Dashboard</strong>, complete management of your <strong>expenses and income</strong>,
            organization of your <strong>animal batches</strong>, tracking of <strong>medical events</strong>, <strong>production</strong> and much more!
          </p>
        </div>
      </div>
    </div>

    <div class="row g-4 justify-content-center">
      <div class="col-12 col-sm-8 col-md-6 col-lg-4" v-for="plan in plans" :key="plan.id">
        <div
          class="card h-100 border-0 shadow"
          style="border-radius: 20px; background-color: #f8f9fa;"
        >
          <div class="card-body text-center px-4 py-4">
            <h5 class="card-title text-success fw-semibold mb-3">{{ plan.name }}</h5>
            <p class="card-text mb-2">
              <strong>Price:</strong> €{{ plan.price }}
            </p>
            <p class="card-text mb-4">
              <strong>Duration:</strong> {{ plan.duration_days }} days
            </p>
            <RouterLink
              :to="`/plans/subscribe/${plan.id}`"
              class="btn text-white w-100 rounded-pill"
              style="background-color: #f38b2c;"
            >
              Choose this plan
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
    console.error('Error loading plans:', error)
  }
})
</script>