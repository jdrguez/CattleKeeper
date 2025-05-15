<template>
  <div v-if="animal">
    <h2>Detalle del animal</h2>
    <p><strong>Identificador:</strong> {{ animal.identifier }}</p>
    <p><strong>Peso:</strong> {{ animal.weight }} kg</p>
    <p><strong>Fecha de nacimiento:</strong> {{ animal.birth_date }}</p>
    <p><strong>Salud:</strong> {{ animal.health_status }}</p>
    <p><strong>Notas:</strong> {{ animal.notes }}</p>

    <h3 class="mt-4">Eventos de Salud</h3>
    <router-link
      :to="{
        name: 'HealthEventCreate',
        params: { batch_slug, animal_slug }
      }"
    >
      <button>➕ Añadir Evento de Salud</button>
    </router-link>

    <ul v-if="healthEvents.length">
      <li v-for="event in healthEvents" :key="event.id" class="mb-2">
        <strong>{{ event.event_type }}</strong> - {{ event.date }}<br />
        {{ event.description }}<br />
        <span v-if="event.veterinarian">👨‍⚕️ {{ event.veterinarian }}</span><br />
        <button @click="deleteHealthEvent(event.id)">🗑️ Eliminar</button>
      </li>
    </ul>
    <p v-else>No hay eventos registrados.</p>
  </div>

  <button @click="$router.push({ name: 'AnimalDelete', params: { batch_slug, animal_slug } })">
    Eliminar Animal
  </button>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import api from '@/api/axios'

const route = useRoute()
const animal = ref(null)
const healthEvents = ref([])

const batch_slug = route.params.batch_slug
const animal_slug = route.params.animal_slug

const fetchHealthEvents = async () => {
  try {
    const healthRes = await api.get(`/api/farm/batch/${batch_slug}/animals/${animal_slug}/health/`)
    console.log('Eventos recibidos:', healthRes.data)
    healthEvents.value = healthRes.data || []
  } catch (error) {
    console.error('Error al obtener eventos:', error)
    healthEvents.value = []
  }
}

onMounted(async () => {
  try {
    const animalRes = await api.get(`/api/farm/batch/${batch_slug}/animals/${animal_slug}/`)
    animal.value = animalRes.data
    await fetchHealthEvents()
  } catch (error) {
    console.error('Error al cargar animal:', error)
  }
})

const deleteHealthEvent = async (eventId) => {
  try {
    await api.post(`/api/farm/batch/${batch_slug}/animals/${animal_slug}/health/${eventId}/delete/`)
    await fetchHealthEvents()
  } catch (error) {
    console.error('Error al eliminar evento:', error)
  }
}
</script>
