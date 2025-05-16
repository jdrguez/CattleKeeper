<template>

   


    <div class="container py-5">
      <div class="card shadow-sm mx-auto" style="max-width: 600px;">
        <div class="card-body">
          <h2 class="card-title text-center mb-4">Perfil de Usuario</h2>
  
          <div v-if="user">
            <div class="text-center mb-4">
              <img
                v-if="user.profile.avatar"
                :src="user.profile.avatar"
                alt="Avatar"
                class="rounded-circle border border-primary"
                style="width: 128px; height: 128px; object-fit: cover;"
              />
              <h3 class="mt-3">{{ user.username }}</h3>
            </div>
  
            <ul class="list-group list-group-flush mb-4">
              <li class="list-group-item d-flex justify-content-between">
                <strong>Nombre:</strong>
                <span>{{ user.first_name }}</span>
              </li>
              <li class="list-group-item d-flex justify-content-between">
                <strong>Apellido:</strong>
                <span>{{ user.last_name }}</span>
              </li>
              <li class="list-group-item d-flex justify-content-between">
                <strong>Email:</strong>
                <span>{{ user.email }}</span>
              </li>
              <li class="list-group-item">
                <strong>Biografía:</strong>
                <p class="mb-0 mt-1">{{ user.profile.bio }}</p>
              </li>
            </ul>
  
            <div class="text-center mb-4">
              <RouterLink
                to="/account/edit"
                class="btn btn-success px-4"
                id="btn_editar"
              >
                Editar Perfil
              </RouterLink>
            </div>
            




            <div>
                <h4>Mis Órdenes</h4>

                <div v-if="loadingOrders" class="text-center mb-3">
                    Cargando órdenes...
                </div>

                <template v-else>
                    <ul v-if="orders.length" class="list-group mb-4">
                        <li
                            class="list-group-item"
                            v-for="order in orders"
                            :key="order.id"
                            @click="goToOrderDetail(order.id)"
                            style="cursor: pointer;"
                            >
                            <strong>Orden #{{ order.id }}</strong> - Estado: {{ order.status }}
                            <ul class="mt-2">
                                <li v-for="(product, idx) in order.products" :key="idx">
                                {{ product.name }} - {{ product.price }}€
                                </li>
                            </ul>
                        </li>
                    </ul>
                    <p v-else>No tienes órdenes aún.</p>
                </template>
                </div>
            <br>
            <br>
          </div>
  
          <div v-else class="text-center text-muted">
            Cargando datos del usuario...
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { RouterLink, useRouter  } from 'vue-router'
  import { onMounted, ref } from 'vue'
  import api from '@/api/axios'

  
  const user = ref(null)
  const orders = ref([])
  const loadingOrders = ref(false)
  
  const router = useRouter()

  function goToOrderDetail(orderId) {
    if (!orderId) return
    router.push({ name: 'order', params: { id: orderId } })

    }




  onMounted(async () => {
    try {
      const responseUser = await api.get('/api/accounts/me/')
      user.value = responseUser.data
  
      loadingOrders.value = true
      const responseOrders = await api.get('/api/orders/')
      orders.value = responseOrders.data
    } catch (error) {
      console.error('Error al obtener datos:', error)
    } finally {
      loadingOrders.value = false
    }
  })

  </script>
  
  <style>
  #btn-editar {
    color: #015730;
  }
  </style>
  