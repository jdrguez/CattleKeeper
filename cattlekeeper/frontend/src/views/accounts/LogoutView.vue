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
  <div class="page-container">
    <div class="confirmation-card">
      <h3 class="confirmation-title">Confirm Logout</h3>
      <p class="confirmation-message">Are you sure you want to log out?</p>
      
      <div class="confirmation-actions">
        <button 
          @click="$router.back()" 
          class="btn btn-secondary"
        >
          Cancel
        </button>
        <button 
          @click="logout" 
          class="btn btn-danger"
        >
          Log Out
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.page-container {
  margin: 2rem auto;
  background: #fff;
  padding: 2rem 2.5rem;
  border-radius: 14px;
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #2d3a45;
  max-width: 600px;
}

.confirmation-card {
  background: #f6f9fc;
  padding: 2rem;
  border-radius: 14px;
  box-shadow: inset 2px 2px 6px #d9e6f0, inset -2px -2px 6px #ffffff;
}

.confirmation-title {
  font-size: 1.8rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: #2d3a45;
  text-align: center;
}

.confirmation-message {
  font-size: 1.1rem;
  margin-bottom: 2rem;
  text-align: center;
  color: #4a5568;
}

.confirmation-actions {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  padding-top: 1.5rem;
  border-top: 2px solid #d4edda;
}

.btn {
  padding: 0.55rem 1.6rem;
  font-weight: 700;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  transition: all 0.3s ease;
  min-width: 120px;
}

.btn-secondary {
  background: #ebf2ff;
  color: #1e7e34;
}

.btn-secondary:hover {
  background: #c5d8ff;
}

.btn-danger {
  background: linear-gradient(135deg, #e53e3e, #c53030);
  color: white;
  box-shadow: 0 6px 16px rgba(229, 62, 62, 0.5);
}

.btn-danger:hover {
  background: linear-gradient(135deg, #c53030, #e53e3e);
  box-shadow: 0 8px 24px rgba(229, 62, 62, 0.8);
}
</style>

