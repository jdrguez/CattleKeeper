<script setup>
import { ref } from 'vue';
import api from '@/api/axios';
import { useRouter } from 'vue-router';
import { useToast } from 'vue-toastification';

const toast = useToast()

const router = useRouter();

const form = ref({
  species: '',
  purchase_date: '',
  quantity: '',
  sex: 3, 
  origin: '',
  notes: ''
});

const speciesOptions = [
  { value: 1, label: 'Cattle' },
  { value: 2, label: 'Poultry' },
  { value: 3, label: 'Pig' },
  { value: 4, label: 'Sheep' },
  { value: 5, label: 'Goat' },
  { value: 99, label: 'Other' }
];

const sexOptions = [
  { value: 1, label: 'Male' },
  { value: 2, label: 'Female' },
  { value: 3, label: 'Mixed' }
];


const createBatch = async () => {
  try {
    await api.post('api/farm/batch/create/', form.value);
    router.push({ name: 'batch-list'});
    toast.success('The batch has been created successfully.')
  } catch (error) {
    console.error('Error al crear el lote:', error);
    toast.error('The batch could not be created.')
  }
};
</script>

<template>
  <div class="page-container">
    <h1 class="page-title">Create New Batch</h1>

    <form @submit.prevent="createBatch" class="form-content">
      <div class="form-grid">
        <div class="form-group">
          <label class="form-label">Species <span class="text-danger">*</span></label>
          <select v-model="form.species" class="form-select" required>
            <option value="" disabled>Select species...</option>
            <option
              v-for="option in speciesOptions"
              :key="option.value"
              :value="option.value"
            >
              {{ option.label }}
            </option>
          </select>
        </div>

        <div class="form-group">
          <label class="form-label">Purchase Date <span class="text-danger">*</span></label>
          <input
            type="date"
            v-model="form.purchase_date"
            class="form-control"
            required
          />
        </div>

        <div class="form-group">
          <label class="form-label">Quantity <span class="text-danger">*</span></label>
          <input
            type="number"
            v-model="form.quantity"
            class="form-control"
            min="1"
            required
          />
        </div>

        <div class="form-group">
          <label class="form-label">Sex</label>
          <select v-model="form.sex" class="form-select">
            <option
              v-for="option in sexOptions"
              :key="option.value"
              :value="option.value"
            >
              {{ option.label }}
            </option>
          </select>
        </div>

        <div class="form-group">
          <label class="form-label">Origin</label>
          <input
            type="text"
            v-model="form.origin"
            class="form-control"
            placeholder="Optional"
          />
        </div>

        <div class="form-group full-width">
          <label class="form-label">Notes</label>
          <textarea
            v-model="form.notes"
            class="form-control"
            rows="4"
            placeholder="Add additional details..."
          ></textarea>
        </div>
      </div>

      <div class="form-actions">
        <button
          type="button"
          class="btn btn-secondary"
          @click="$router.back()"
        >
          Cancel
        </button>
        <button type="submit" class="btn btn-success">
          Create Batch
        </button>
      </div>
    </form>
  </div>
</template>

<style scoped>
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
  user-select: none;
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

.form-select,
.form-control {
  width: 100%;
  padding: 0.5rem 1rem;
  border: 2px solid #cbd5e1;
  border-radius: 12px;
  background: #f9fafb;
  transition: all 0.3s ease;
}

.form-select:focus,
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
</style>