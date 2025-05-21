<template>
  <div class="container py-5" style="max-width: 480px;">
    <h2 class="mb-4 border-bottom pb-2 text-center"> Create Health Event</h2>

    <form @submit.prevent="submitEvent" class="bg-white p-4 rounded-4 shadow-sm">
      <div class="mb-3">
        <label class="form-label fw-semibold" for="date"><i class="bi bi-calendar"></i> Date</label>
        <input
          id="date"
          type="date"
          v-model="form.date"
          required
          class="form-control rounded-pill border-primary"
          style="box-shadow: inset 0 1px 3px rgb(0 0 0 / 0.1);"
          aria-required="true"
        />
      </div>

      <div class="mb-3">
        <label class="form-label fw-semibold" for="event_type"><i class="bi bi-list-check"></i> Event Type</label>
        <select
          id="event_type"
          v-model="form.event_type"
          required
          class="form-select rounded-pill border-primary"
          style="box-shadow: inset 0 1px 3px rgb(0 0 0 / 0.1);"
          aria-required="true"
        >
          <option disabled value="">Select type</option>
          <option value="VACCINE">Vaccine</option>
          <option value="ILLNESS">Illness</option>
          <option value="CHECKUP">Checkup</option>
          <option value="SURGERY">Surgery</option>
        </select>
      </div>

      <div class="mb-3">
        <label class="form-label fw-semibold" for="description"><i class="bi bi-card-text"></i> Description</label>
        <textarea
          id="description"
          v-model="form.description"
          required
          class="form-control rounded-3 border-secondary"
          rows="4"
          style="resize: vertical;"
          aria-required="true"
        ></textarea>
      </div>

      <div class="mb-4">
        <label class="form-label fw-semibold" for="veterinarian"><i class="bi bi-person-badge"></i> Veterinarian (optional)</label>
        <input
          id="veterinarian"
          type="text"
          v-model="form.veterinarian"
          class="form-control rounded-pill border-primary"
          style="box-shadow: inset 0 1px 3px rgb(0 0 0 / 0.1);"
          placeholder="Veterinarian name"
        />
      </div>

      <button
        type="submit"
        class="btn btn-primary w-100 rounded-pill shadow-sm fw-bold"
      >
        Save
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '@/api/axios'
import { useToast } from 'vue-toastification';

const toast = useToast()
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
  toast.success('The health event has been created successfully.')
}
</script>

<style scoped>
.health-event-container {
  background: #fff;
  border-radius: 14px;
  box-shadow:
    0 4px 12px rgba(0, 0, 0, 0.08),
    0 1px 4px rgba(0, 0, 0, 0.06);
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
