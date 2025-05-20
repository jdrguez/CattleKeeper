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
  <div
    class="d-flex justify-content-center align-items-center"
  >
    <div
      class="card shadow-lg p-4 text-center"
      style="width: 100%; max-width: 400px; border-radius: 20px; background-color: white; color: black;"
    >
      <h4 class="mb-4">¿Seguro que deseas cerrar la sesión?</h4>
      <button
        @click="logout"
        class="btn rounded-pill text-white"
        style="background-color: #f38b2c; padding: 0.5rem 1.5rem; width: 100%;"
      >
        Cerrar sesión
      </button>
    </div>
  </div>
</template>
