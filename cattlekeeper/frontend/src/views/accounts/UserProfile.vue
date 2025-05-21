<template>
  <div class="page-container">
    <div class="profile-grid">
      <div class="profile-card">
        <div v-if="user">
          <div class="text-center mb-4">
            <img
              v-if="user.profile.avatar"
              :src="user.profile.avatar"
              alt="Avatar"
              class="profile-avatar"
            />
            <h3 class="profile-username">
              {{ user.username }}
            </h3>
          </div>

          <div class="profile-details">
            <div class="profile-detail-item">
              <span class="detail-label">First Name:</span>
              <span class="detail-value">{{ user.first_name }}</span>
            </div>
            <div class="profile-detail-item">
              <span class="detail-label">Last Name:</span>
              <span class="detail-value">{{ user.last_name }}</span>
            </div>
            <div class="profile-detail-item">
              <span class="detail-label">Email:</span>
              <span class="detail-value">{{ user.email }}</span>
            </div>
            <div class="profile-detail-item">
              <span class="detail-label">Bio:</span>
              <p class="detail-bio">{{ user.profile.bio }}</p>
            </div>
          </div>

          <div class="profile-actions">
            <RouterLink
              to="/account/edit"
              class="btn btn-success"
              id="btn_editar"
            >
              Edit Profile
            </RouterLink>
          </div>
        </div>

        <div v-else class="loading-message">
          Loading user data...
        </div>
      </div>

      <div class="subscription-card">
        <ActiveSubscripcion />
        <CancelSubscripcion v-if="isActive"/>
      </div>
    </div>
  </div>
</template>

<style scoped>
.page-container {
  margin: 2rem auto;
  padding: 2rem 2.5rem;
  max-width: 1200px;
}

.profile-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.profile-card,
.subscription-card {
  background: #fff;
  padding: 2rem;
  border-radius: 14px;
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}

.profile-avatar {
  width: 130px;
  height: 130px;
  object-fit: cover;
  border-radius: 50%;
  border: 3px solid #28a745;
}

.profile-username {
  margin-top: 1rem;
  font-weight: 600;
  color: #2d3a45;
}

.profile-details {
  margin-bottom: 2rem;
}

.profile-detail-item {
  padding: 1rem 0;
  border-bottom: 1px solid #e9ecef;
  display: flex;
  justify-content: space-between;
}

.detail-label {
  font-weight: 600;
  color: #4a5568;
}

.detail-value {
  color: #2d3a45;
}

.detail-bio {
  margin-top: 0.5rem;
  color: #6b7280;
  font-style: italic;
}

.profile-actions {
  text-align: center;
  margin-bottom: 2rem;
}

.btn-success {
  background: linear-gradient(135deg, #28a745, #1e7e34);
  color: white;
  padding: 0.55rem 1.6rem;
  border-radius: 30px;
  font-weight: 700;
  box-shadow: 0 6px 16px rgba(30, 126, 52, 0.5);
}

.loading-message {
  text-align: center;
  color: #6b7280;
  font-style: italic;
}

/* Responsive layout */
@media (max-width: 768px) {
  .profile-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<script setup>
import { ref, onMounted } from 'vue'
import { storeToRefs } from 'pinia'
import { useSubscriptionStore } from '@/stores/subscription'
import api from '@/api/axios'

import ActiveSubscripcion from '@/components/subscripcion/ActiveSubscripcion.vue'
import CancelSubscripcion from '@/components/subscripcion/CancelSubscripcion.vue'

const subscripcion = useSubscriptionStore()
const { isActive } = storeToRefs(subscripcion)

const user = ref(null)

onMounted(async () => {
  try {
    await subscripcion.checkSubscription()

    const responseUser = await api.get('/api/accounts/me/')
    user.value = responseUser.data
  } catch (error) {
    console.error('Error al obtener datos del usuario o suscripción:', error)
  }
})
</script>
