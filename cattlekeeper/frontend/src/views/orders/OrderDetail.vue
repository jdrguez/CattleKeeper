<template>
    <div class="container py-5">
      <div class="card mx-auto shadow-sm" style="max-width: 600px;">
        <div class="card-body">
          <h3 class="card-title mb-4">Detalle de la Orden #{{ orderId }}</h3>
  
          <div v-if="loading">Cargando detalle...</div>
          <div v-else-if="order">
            <p><strong>Estado:</strong> {{ order.status }}</p>
            <p><strong>Total:</strong> {{ order.price }} €</p>
            <p><strong>Creado el:</strong> {{ new Date(order.created_at).toLocaleString() }}</p>
  
            <h5 class="mt-4">Productos:</h5>
            <ul>
              <li v-for="(product, i) in order.products" :key="i">
                {{ product.name }} - {{ product.price }} €
              </li>
            </ul>
          </div>
          <div v-else class="text-danger">No se pudo cargar la orden.</div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { onMounted, ref } from 'vue'
  import { useRoute } from 'vue-router'
  import api from '@/api/axios'
  
  const route = useRoute()
  const orderId = route.params.id
  
  const order = ref(null)
  const loading = ref(true)
  
  onMounted(async () => {
    try {
      const response = await api.get(`/api/orders/${orderId}/`)
      order.value = response.data
    } catch (error) {
      console.error('Error al cargar orden:', error)
    } finally {
      loading.value = false
    }
  })
  </script>
  