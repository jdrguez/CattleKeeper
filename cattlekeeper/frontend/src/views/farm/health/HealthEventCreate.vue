<template>
  <div class="health-event-container mx-auto p-4" style="max-width: 480px;">
    <h2 class="mb-4 text-primary fw-bold border-bottom pb-2">Crear Evento de Salud</h2>
    <form @submit.prevent="submitEvent" novalidate>
      <div class="form-group mb-3">
        <label class="form-label">Fecha:</label>
        <input
          type="date"
          v-model="form.date"
          required
          class="form-control input-custom"
          aria-required="true"
        />
      </div>

      <div class="form-group mb-3">
        <label class="form-label">Tipo de Evento:</label>
        <select
          v-model="form.event_type"
          required
          class="form-select input-custom"
          aria-required="true"
        >
          <option disabled value="">Selecciona tipo</option>
          <option value="VACCINE">Vacuna</option>
          <option value="ILLNESS">Enfermedad</option>
          <option value="CHECKUP">Chequeo</option>
          <option value="SURGERY">Cirugía</option>
        </select>
      </div>

      <div class="form-group mb-3">
        <label class="form-label">Descripción:</label>
        <textarea
          v-model="form.description"
          required
          class="form-control input-custom"
          rows="4"
          aria-required="true"
        ></textarea>
      </div>

      <div class="form-group mb-4">
        <label class="form-label">Veterinario (opcional):</label>
        <input
          type="text"
          v-model="form.veterinarian"
          class="form-control input-custom"
          placeholder="Nombre del veterinario"
        />
      </div>

      <button type="submit" class="btn btn-primary w-100 fw-semibold shadow-sm">
        Guardar
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '@/api/axios'

const route = useRoute()
const router = useRouter()
const { batch_slug, animal_slug } = route.params

const form = ref({
  date: '',
  event_type: '',
  description: '',
  veterinarian: ''
})

const submitEvent = async () => {
  await api.post(`/api/farm/batch/${batch_slug}/animals/${animal_slug}/health/create/`, form.value)
  router.push({ name: 'AnimalDetail', params: { batch_slug, animal_slug } })
}
</script>

<style scoped>
.health-event-container {
  background: #fff;
  border-radius: 14px;
  box-shadow:
    0 4px 12px rgba(0, 0, 0, 0.08),
    0 1px 4px rgba(0, 0, 0, 0.06);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.form-label {
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 6px;
  display: inline-block;
}

.input-custom {
  border: 1.8px solid #cbd5e1;
  border-radius: 10px;
  padding: 10px 14px;
  font-size: 1rem;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
  background: #fefefe;
}

.input-custom:focus {
  outline: none;
  border-color: #4a90e2;
  box-shadow: 0 0 8px rgba(74, 144, 226, 0.4);
  background: #fff;
}

.btn-primary {
  border-radius: 10px;
  padding: 12px 0;
  font-size: 1.1rem;
  letter-spacing: 0.04em;
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
}

.btn-primary:hover,
.btn-primary:focus {
  background-color: #357abd;
  box-shadow: 0 4px 12px rgba(53, 122, 189, 0.4);
  outline: none;
}
</style>
