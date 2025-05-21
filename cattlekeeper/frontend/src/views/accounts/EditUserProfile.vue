<template>
  <div class="page-container">
    <h1 class="page-title">Edit Profile</h1>
    
    <div class="form-content">
      <form @submit.prevent="saveProfile" class="form-grid">
        <div class="form-group">
          <label class="form-label">First Name <span class="text-danger">*</span></label>
          <input
            type="text"
            v-model="form.first_name"
            class="form-control"
            placeholder="Your first name"
            required
          />
        </div>

        <div class="form-group">
          <label class="form-label">Last Name <span class="text-danger">*</span></label>
          <input
            type="text"
            v-model="form.last_name"
            class="form-control"
            placeholder="Your last name"
            required
          />
        </div>

        <div class="form-group full-width">
          <label class="form-label">Email <span class="text-danger">*</span></label>
          <input
            type="email"
            v-model="form.email"
            class="form-control"
            placeholder="your@email.com"
            required
          />
        </div>

        <div class="form-group full-width">
          <label class="form-label">Bio</label>
          <textarea
            v-model="form.bio"
            class="form-control"
            rows="4"
            placeholder="Tell us about yourself..."
          ></textarea>
        </div>

        <div class="form-group full-width">
          <label class="form-label">Profile Picture</label>
          <input
            type="file"
            @change="handleFileUpload"
            accept="image/*"
            class="form-control"
          />
        </div>

        <div class="form-actions">
          <button type="button" class="btn btn-secondary" @click="$router.back()">
            Cancel
          </button>
          <button type="submit" class="btn btn-success">
            Save Changes
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api/axios';
import { useToast } from 'vue-toastification';
import { useRouter } from 'vue-router';

const toast = useToast()
const router = useRouter()

const form = ref({
  first_name: '',
  last_name: '',
  email: '',
  bio: '',
})
const avatarFile = ref(null)

const loadProfile = async () => {
  try {
    const { data } = await api.get('/api/accounts/me/')
    form.value.first_name = data.first_name
    form.value.last_name = data.last_name
    form.value.email = data.email
    form.value.bio = data.profile.bio
  } catch (error) {
    console.error('Error loading profile data:', error)
    toast.error('Failed to load profile data')
  }
}

const handleFileUpload = (e) => {
  avatarFile.value = e.target.files[0]
}

const saveProfile = async () => {
  const formData = new FormData()
  formData.append('first_name', form.value.first_name)
  formData.append('last_name', form.value.last_name)
  formData.append('email', form.value.email)
  formData.append('bio', form.value.bio)
  if (avatarFile.value) {
    formData.append('avatar', avatarFile.value)
  }

  try {
    await api.post('/api/accounts/user/edit/', formData)
    router.push('/account')
    toast.success('Profile updated successfully')
  } catch (error) {
    console.error('Error updating profile:', error)
    toast.error('Failed to update profile')
  }
}

onMounted(loadProfile)
</script>

<style scoped>
/* Your existing form styles from other components */
.page-container {
  margin: 2rem auto;
  background: #fff;
  padding: 2rem 2.5rem;
  border-radius: 14px;
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #2d3a45;
}

.page-title {
  font-size: 2.1rem;
  font-weight: 700;
  border-bottom: 3px solid #28a745;
  padding-bottom: 0.3rem;
  margin-bottom: 1.8rem;
  letter-spacing: 0.03em;
}

.form-content {
  background: #f6f9fc;
  padding: 1.5rem;
  border-radius: 14px;
  box-shadow: inset 2px 2px 6px #d9e6f0, inset -2px -2px 6px #ffffff;
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group.full-width {
  grid-column: 1 / -1;
}

.form-label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #34495e;
}

.form-control {
  width: 100%;
  padding: 0.5rem 1rem;
  border: 2px solid #cbd5e1;
  border-radius: 12px;
  background: #f9fafb;
  transition: all 0.3s ease;
}

.form-control:focus {
  outline: none;
  border-color: #28a745;
  box-shadow: 0 0 8px #33d459;
}

textarea.form-control {
  min-height: 120px;
  resize: vertical;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  padding-top: 1rem;
  border-top: 2px solid #d4edda;
}

.btn {
  padding: 0.55rem 1.6rem;
  font-weight: 700;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-secondary {
  background: #ebf2ff;
  color: #1e7e34;
}

.btn-secondary:hover {
  background: #c5d8ff;
}

.btn-success {
  background: linear-gradient(135deg, #28a745, #1e7e34);
  color: white;
  box-shadow: 0 6px 16px rgba(30, 126, 52, 0.5);
}

.btn-success:hover {
  background: linear-gradient(135deg, #1e7e34, #28a745);
  box-shadow: 0 8px 24px rgba(30, 126, 52, 0.8);
}

.text-danger {
  color: #e53e3e;
}
</style>