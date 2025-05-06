<script setup>
import { inject } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()


const logout = async () => {
  localStorage.removeItem('token')  
  auth.isLoggedIn = false; 

  await router.push('/dashboard')
  window.location.reload()
}
</script>

<template>
  <button @click="logout">Cerrar sesión</button>
</template>
