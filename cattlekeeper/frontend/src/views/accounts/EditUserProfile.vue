<template>
    <div class="max-w-xl mx-auto p-4">
      <h2 class="text-2xl font-bold mb-4">Editar Perfil</h2>
      <form @submit.prevent="guardarPerfil">
        <div class="mb-4">
          <label class="block">Nombre</label>
          <input v-model="form.first_name" class="w-full border rounded p-2" />
        </div>
        <div class="mb-4">
          <label class="block">Apellido</label>
          <input v-model="form.last_name" class="w-full border rounded p-2" />
        </div>
        <div class="mb-4">
          <label class="block">Email</label>
          <input v-model="form.email" type="email" class="w-full border rounded p-2" />
        </div>
        <div class="mb-4">
          <label class="block">Biografía</label>
          <textarea v-model="form.bio" class="w-full border rounded p-2"></textarea>
        </div>
        <div class="mb-4">
          <label class="block">Avatar</label>
          <input type="file" @change="handleFileUpload" class="w-full" />
        </div>
        <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded">Guardar</button>
      </form>
      <p v-if="mensaje" class="mt-4 text-green-600">{{ mensaje }}</p>
    </div>
  </template>
  
  <script setup>
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
      const { data } = await api.get('/api/accounts/admin/')
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
  