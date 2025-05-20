<template>
  <div class="container py-8">
    <div
      class="card shadow-sm mx-auto"
      style="max-width: 600px; border-radius: 1rem; background-color: #fff;"
    >
      <div class="card-body px-5 py-4">
        <h2
          class="card-title text-center mb-4 fw-bold text-secondary"
        >
          Perfil de Usuario
        </h2>

        <div v-if="user">
          <div class="text-center mb-4">
            <img
              v-if="user.profile.avatar"
              :src="user.profile.avatar"
              alt="Avatar"
              class="rounded-circle border border-3 border-success"
              style="width: 130px; height: 130px; object-fit: cover;"
            />
            <h3 class="mt-3 fw-semibold text-dark">
              {{ user.username }}
            </h3>
          </div>

          <ul class="list-group list-group-flush mb-4">
            <li
              class="list-group-item d-flex justify-content-between align-items-center"
              style="border: none; border-bottom: 1px solid #e9ecef;"
            >
              <span class="fw-semibold text-secondary">Nombre:</span>
              <span class="text-dark">{{ user.first_name }}</span>
            </li>
            <li
              class="list-group-item d-flex justify-content-between align-items-center"
              style="border: none; border-bottom: 1px solid #e9ecef;"
            >
              <span class="fw-semibold text-secondary">Apellido:</span>
              <span class="text-dark">{{ user.last_name }}</span>
            </li>
            <li
              class="list-group-item d-flex justify-content-between align-items-center"
              style="border: none; border-bottom: 1px solid #e9ecef;"
            >
              <span class="fw-semibold text-secondary">Email:</span>
              <span class="text-dark">{{ user.email }}</span>
            </li>
            <li
              class="list-group-item"
              style="border: none;"
            >
              <span class="fw-semibold text-secondary">Biografía:</span>
              <p class="mb-0 mt-1 text-muted fst-italic">{{ user.profile.bio }}</p>
            </li>
          </ul>

          <div class="text-center mb-4">
            <RouterLink
              to="/account/edit"
              class="btn btn-success rounded-pill px-4 py-2 fw-semibold shadow-sm"
              id="btn_editar"
              @mouseover="hover = true"
              @mouseleave="hover = false"
              :style="hover ? 'background-color: #0b5222;' : ''"
            >
              Editar Perfil
            </RouterLink>
          </div>

          <div>
            <ActiveSubscripcion />
          </div>
        </div>

        <div
          v-else
          class="text-center text-muted fst-italic"
        >
          Cargando datos del usuario...
        </div>
      </div>
    </div>
  </div>
</template>


<script setup>
import { RouterLink } from 'vue-router'
import { onMounted, ref } from 'vue'
import api from '@/api/axios'
import ActiveSubscripcion from '@/components/subscripcion/ActiveSubscripcion.vue'

const user = ref(null)

onMounted(async () => {
  try {
    const responseUser = await api.get('/api/accounts/me/')
    user.value = responseUser.data
  } catch (error) {
    console.error('Error al obtener datos del usuario:', error)
  }
})
</script>

<style>
#btn-editar {
  color: #015730;
}
</style>
