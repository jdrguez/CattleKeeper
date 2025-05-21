<template>
  <div class="container py-5">
    <div class="d-flex justify-content-between align-items-center mb-5">
      <h1 class="fw-bold text-primary-emphasis">Batch List</h1>
      <router-link to="/batch/create" class="btn btn-success btn-lg shadow">
        +
      </router-link>
    </div>

<div class="row g-4">
  <div
    v-for="batch in batches"
    :key="batch.slug"
    class="col-12 col-md-6 col-lg-4"
  >
    <div class="card h-100 rounded-4 shadow-sm border-0" style="background-color: #f9f9fb;">
      <div class="card-body d-flex flex-column justify-content-between">
        <div>
          <h4 class="fw-semibold text-secondary-emphasis mb-3">{{ batch.name }}</h4>
          <ul class="list-unstyled text-muted">
            <li class="d-flex align-items-center mb-1">
              <i class="bi bi-patch-question me-2 text-secondary"></i>
              <strong class="me-1">Species:</strong> {{ batch.species }}
            </li>
            <li class="d-flex align-items-center mb-1">
              <i class="bi bi-gender-ambiguous me-2 text-secondary"></i>
              <strong class="me-1">Sex:</strong> {{ batch.sex }}
            </li>
            <li class="d-flex align-items-center">
              <i class="bi bi-123 me-2 text-secondary"></i>
              <strong class="me-1">Quantity:</strong> {{ batch.quantity }}
            </li>
          </ul>
        </div>
        <button
          class="btn btn-outline-primary mt-4 rounded-pill w-100 shadow-sm"
          @click="goToDetail(batch.slug)"
        >
          View Details
        </button>
      </div>
    </div>
  </div>
</div>

  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import api from '@/api/axios';

const batches = ref([]);
const router = useRouter();



onMounted(async () => {
  try {
    const response = await api.get('api/farm/batch/');
    batches.value = response.data;
  } catch (error) {
    console.error('Error fetching batches:', error);
  }
});

const goToDetail = (slug) => {
  router.push({ name: 'BatchDetail', params: { batch_slug: slug } });
};
</script>
