<template>
    <div class="d-flex flex-column justify-content-center align-items-center vh-100 text-center bg-light text-dark p-4">
      <div class="card shadow p-4" style="max-width: 500px;">
        <div class="card-body">
          <h1 class="display-5 mb-3">
            <i class="bi bi-exclamation-triangle-fill text-warning me-2"></i>
            ¡Vaya! 😕
          </h1>
          <p class="lead mb-4">
            El servidor está caído en estos momentos. Por favor, prueba a reiniciar la página más tarde.
          </p>
          <button class="btn btn-primary" @click="reloadPage">
            <i class="bi bi-arrow-clockwise me-2"></i>
            Reintentar
          </button>
        </div>
      </div>
    </div>
  </template>
  
<script setup>
import {useRouter} from 'vue-router';
const router = useRouter()

function reloadPage() {
    router.push('/account')
}
</script>