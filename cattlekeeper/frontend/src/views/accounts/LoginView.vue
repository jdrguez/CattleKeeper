<script setup lang="ts">
import { ref, inject } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const router = useRouter()
const backendUrl = 'http://127.0.0.1:8000' 
const auth = inject<{ isLoggedIn: boolean }>('auth')!

const login = async () => {
    try {
        const response = await axios.post(`${backendUrl}/api/accounts/login/`, {
            username: username.value,
            password: password.value
        })
  
        const token = response.headers['authorization']
        localStorage.setItem('token', token) 
  
        auth.isLoggedIn = true

        await router.push('/dashboard')
    } catch (err) {
        alert('Credenciales inválidas')
        console.error(err)
    }
}
</script>

<template>
  <form @submit.prevent="login">
    <input v-model="username" placeholder="Usuario" />
    <input v-model="password" type="password" placeholder="Contraseña" />
    <button type="submit">Iniciar sesión</button>
  </form>
</template>
