<template>
  <div v-if="animal" class="container py-5">
    <h2 class="fw-bold text-primary mb-4 border-bottom pb-2">🐄 Detalle del Animal</h2>

    <div class="card shadow-sm border-0 rounded-4 p-4 mb-4" style="background-color: #fdfdfd;">
      <div class="row">
        <div class="col-md-6">
          <p><strong>🔖 Identificador:</strong> {{ animal.identifier }}</p>
          <p><strong>⚖️ Peso:</strong> {{ animal.weight }} kg</p>
        </div>
        <div class="col-md-6">
          <p><strong>🎂 Fecha de nacimiento:</strong> {{ animal.birth_date }}</p>
          <p><strong>❤️ Salud:</strong> {{ animal.health_status }}</p>
        </div>
        <div class="col-12">
          <p><strong>📝 Notas:</strong> {{ animal.notes || 'N/A' }}</p>
        </div>
      </div>
    </div>

    <div class="d-flex justify-content-between align-items-center mb-3">
      <h3 class="text-secondary fw-semibold mb-0">📋 Eventos de Salud</h3>
      <router-link
        :to="{ name: 'HealthEventCreate', params: { batch_slug, animal_slug } }"
        class="btn btn-outline-success rounded-pill shadow-sm"
      >
        ➕ Añadir Evento
      </router-link>
    </div>

    <div v-if="healthEvents.length" class="list-group mb-4">
      <div
        v-for="event in healthEvents"
        :key="event.id"
        class="list-group-item list-group-item-action mb-2 rounded-3 shadow-sm"
      >
        <div class="d-flex justify-content-between align-items-start">
          <div>
            <h6 class="mb-1">{{ event.event_type }} <small class="text-muted">({{ event.date }})</small></h6>
            <p class="mb-1">{{ event.description }}</p>
            <small v-if="event.veterinarian" class="text-muted">👨‍⚕️ {{ event.veterinarian }}</small>
          </div>
          <button
            @click="deleteHealthEvent(event.id)"
            class="btn btn-sm btn-outline-danger rounded-circle"
            title="Eliminar evento"
          >
            🗑️
          </button>
        </div>
      </div>
    </div>

    <p v-else class="text-muted fst-italic">No hay eventos registrados.</p>

    <button
      class="btn btn-outline-danger mt-3 rounded-pill shadow-sm"
      @click="$router.push({ name: 'AnimalDelete', params: { batch_slug, animal_slug } })"
    >
      🐄 Eliminar Animal
    </button>
  </div>
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
