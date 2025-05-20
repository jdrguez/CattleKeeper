<template>
  <div class="d-flex align-items-center justify-content-center vh-50 mb-4">
    <div
      class="card shadow-lg p-4"
      style="width: 100%; max-width: 400px; border-radius: 20px; background-color:#015730; color: white; position: relative"
    >
      <h3 class="text-center mb-4">Regístrate</h3>

      <form @submit.prevent="signup">
        <div class="mb-3">
          <label for="username" class="form-label">Usuario</label>
          <input
            v-model="username"
            type="text"
            class="form-control rounded-pill"
            id="username"
            placeholder="Introduce tu usuario"
            required
          />
        </div>

        <div class="mb-3">
          <label for="email" class="form-label">Correo electrónico</label>
          <input
            v-model="email"
            type="email"
            class="form-control rounded-pill"
            id="email"
            placeholder="Introduce tu correo"
            required
          />
        </div>

        <div class="mb-4">
          <label for="password" class="form-label">Contraseña</label>
          <input
            v-model="password"
            type="password"
            class="form-control rounded-pill"
            id="password"
            placeholder="Contraseña"
            required
          />
        </div>

        <button type="submit" class="btn w-100 rounded-pill text-white" style="background-color: #f38b2c">
          Registrarse
        </button>

        <div class="text-center mt-3">
          <RouterLink to="/login" class="text-decoration-none text-warning">¿Ya tienes cuenta? Inicia sesión</RouterLink>
        </div>
      </form>
    </div>
  </div>
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
