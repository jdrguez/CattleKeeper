<template>
  <div class="d-flex align-items-center justify-content-center vh-50 mb-4">
    <div
      class="card shadow-lg p-4"
      style="width: 100%; max-width: 400px; border-radius: 20px; background-color:#015730; color: white; position: relative"
    >
      <h3 class="text-center mb-4">Sign Up</h3>

      <form @submit.prevent="signup">
        <div class="mb-3">
          <label for="username" class="form-label">Username</label>
          <input
            v-model="username"
            type="text"
            class="form-control rounded-pill"
            id="username"
            placeholder="Enter your username"
            required
          />
        </div>

        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input
            v-model="email"
            type="email"
            class="form-control rounded-pill"
            id="email"
            placeholder="Enter your email"
            required
          />
        </div>

        <div class="mb-4">
          <label for="password" class="form-label">Password</label>
          <input
            v-model="password"
            type="password"
            class="form-control rounded-pill"
            id="password"
            placeholder="Password"
            required
          />
        </div>

        <button type="submit" class="btn w-100 rounded-pill text-white" style="background-color: #f38b2c">
          Sign Up
        </button>

        <div class="text-center mt-3">
          <RouterLink to="/login" class="text-decoration-none text-warning">Already have an account? Log in</RouterLink>
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
import { useToast } from 'vue-toastification';

const toast = useToast()

const signup = async () => {
  try {
    const response = await axios.post(`${backendUrl}/api/accounts/signup/`, {
      username: username.value,
      email: email.value,
      password: password.value,
    })

    if (response.status === 200) {
      toast.success('Registration successful! You will be redirected to login.')
      router.push('/login')
    }
  } catch (error) {
    console.error('Error registering user:', error)
    toast.error('There was an error with the registration. Please try again.')
  }
}
</script>