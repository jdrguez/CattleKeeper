<template>
    <div class="max-w-xl mx-auto p-4">
      <h2 class="text-2xl font-bold mb-4">Perfil de Usuario</h2>
      <div v-if="user">
        <p><strong>Usuario:</strong> {{ user.username }}</p>
        <p><strong>Nombre:</strong> {{ user.first_name }}</p>
        <p><strong>Apellido:</strong> {{ user.last_name }}</p>
        <p><strong>Email:</strong> {{ user.email }}</p>
        <p><strong>Biografía:</strong> {{ user.profile.bio }}</p>
        <div v-if="user.profile.avatar">
          <img :src="user.profile.avatar" alt="Avatar" class="w-32 h-32 object-cover rounded-full mt-2" />
        </div>

        <div>
            <RouterLink to="account/edit"> Edita tu perfil</RouterLink>
        </div>

      </div>
      <div v-else>
        <p>Cargando datos del usuario...</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { RouterLink } from 'vue-router'
  import { onMounted, ref } from 'vue'
  import api from '@/api/axios'
  const user = ref(null)
  
  onMounted(async () => {
    try {
      const response = await api.get('/api/accounts/me/')
      user.value = response.data
    } catch (error) {
      console.error('Error al obtener datos del usuario:', error)
    }
  })
  </script>
  