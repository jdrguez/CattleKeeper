<template>

    <div class="container mt-5">
      <div class="card shadow-sm">
        <div class="card-header bg-success text-white">
          <h2 class="mb-0">Editar Perfil</h2>
        </div>
        <div class="card-body">
          <form @submit.prevent="guardarPerfil" class="row g-3">
  
            <div class="col-md-6">
              <label for="firstName" class="form-label">Nombre</label>
              <input
                id="firstName"
                type="text"
                v-model="form.first_name"
                class="form-control"
                placeholder="Tu nombre"
                required
              />
            </div>
  
            <div class="col-md-6">
              <label for="lastName" class="form-label">Apellido</label>
              <input
                id="lastName"
                type="text"
                v-model="form.last_name"
                class="form-control"
                placeholder="Tu apellido"
                required
              />
            </div>
  
            <div class="col-12">
              <label for="email" class="form-label">Email</label>
              <input
                id="email"
                type="email"
                v-model="form.email"
                class="form-control"
                placeholder="correo@ejemplo.com"
                required
              />
            </div>
  
            <div class="col-12">
              <label for="bio" class="form-label">Biografía</label>
              <textarea
                id="bio"
                v-model="form.bio"
                rows="4"
                class="form-control"
                placeholder="Cuéntanos sobre ti..."
              ></textarea>
            </div>
  
            <div class="col-12">
              <label for="avatar" class="form-label">Avatar</label>
              <input
                id="avatar"
                type="file"
                @change="handleFileUpload"
                accept="image/*"
                class="form-control"
              />
            </div>
  
            <div class="col-12 d-flex justify-content-end gap-2">
              <button type="button" class="btn btn-secondary" @click="$router.back()">Cancelar</button>
              <button type="submit" class="btn btn-success">Guardar</button>
            </div>
  
          </form>
  
          <p v-if="mensaje" class="mt-3 text-success fw-semibold">{{ mensaje }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import Breadcrumbs from '@/components/utils/Breadcrumbs.vue';
  import { ref, onMounted } from 'vue'
  import api from '@/api/axios';
  
  const form = ref({
    first_name: '',
    last_name: '',
    email: '',
    bio: '',
  })
  const avatarFile = ref(null)
  const mensaje = ref('')
  
  const cargarDatos = async () => {
    try {
      const { data } = await api.get('/api/accounts/me/')
      form.value.first_name = data.first_name
      form.value.last_name = data.last_name
      form.value.email = data.email
      form.value.bio = data.profile.bio
    } catch (error) {
      console.error('Error al cargar datos del perfil:', error)
    }
  }
  
  const handleFileUpload = (e) => {
    avatarFile.value = e.target.files[0]
  }
  
  const guardarPerfil = async () => {
    const formData = new FormData()
    formData.append('first_name', form.value.first_name)
    formData.append('last_name', form.value.last_name)
    formData.append('email', form.value.email)
    formData.append('bio', form.value.bio)
    if (avatarFile.value) {
      formData.append('avatar', avatarFile.value)
    }
  
    try {
      const response = await api.post('/api/accounts/user/edit/', formData)
      mensaje.value = 'Perfil actualizado correctamente.'
    } catch (error) {
      console.error('Error al actualizar el perfil:', error)
    }
  }
  
  onMounted(cargarDatos)
  </script>
  