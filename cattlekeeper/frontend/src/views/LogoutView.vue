<script setup lang="ts">
import { useRouter } from 'vue-router'
import { inject } from 'vue'

const router = useRouter()
const auth = inject<{ isLoggedIn: boolean }>('auth')!

const logout = async () => {
  localStorage.removeItem('token')
  auth.isLoggedIn = false
  
  await router.push('/login')
}
</script>

<template>
  <button @click="logout">Cerrar sesión</button>
</template>
