<template>
    <form @submit.prevent="signup">
      <input v-model="username" placeholder="Usuario" />
      <input v-model="email" type="email" placeholder="Correo electrónico" />
      <input v-model="password" type="password" placeholder="Contraseña" />
      <button type="submit">Registrarse</button>
    </form>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  import { useRouter } from 'vue-router'
  
  const username = ref('')
  const email = ref('')
  const password = ref('')
  const router = useRouter()
  
  const backendUrl = 'http://127.0.0.1:8000'  
  
  const signup = async () => {
    try {
      
      const response = await axios.post(`${backendUrl}/api/accounts/signup/`, {
        username: username.value,
        email: email.value,
        password: password.value,
      })
  
      if (response.status === 201) {
       
        router.push('/login')
      }
    } catch (error) {
      console.error('Error al registrar el usuario:', error)
      alert('Hubo un error con el registro. Intenta de nuevo.')
    }
  }
  </script>
  