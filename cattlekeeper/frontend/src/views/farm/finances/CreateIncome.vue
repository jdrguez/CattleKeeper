<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import api from '@/api/axios';
import { useToast } from 'vue-toastification';

const toast = useToast();
const router = useRouter();

const form = ref({
  category: '',
  batch: '',
  description: '',
  amount: '',
  currency: '€',
  date: '',
});

const categories = [
  { value: 'SALE', label: 'Sale' },
  { value: 'SUBSIDY', label: 'Subsidy' },
  { value: 'DONATION', label: 'Donation' },
  { value: 'OTHER', label: 'Other' }
];

const batches = ref([]);

const fetchBatches = async () => {
  try {
    const response = await api.get('api/farm/batch/');
    batches.value = response.data;
  } catch(error) {
    if (error.response && error.response.status== 402){
      router.push('/plans')
      toast.error('No tienes subscripción activa');
    }else{
      console.error('Error creando ingreso:', error);
      toast.error('Hubo un error al crear el ingreso');
    }
  }
};

onMounted(() => {
  fetchBatches();
});

const createIncome = async () => {
  try {
    await api.post('api/farm/finances/incomes/create/', form.value);
    toast.success('Income created successfully');
    router.push({ name: 'incomes' });
  }catch(error) {
    if (error.response && error.response.status== 402){
      router.push('/plans')
      toast.error('There was an error creating the Income');
    }else{
      console.error('Error creando ingreso:', error);
      toast.error('There was an error creating the Income');
    }
  }
};
</script>

<template>
  <div class="page-container">
    <h1 class="page-title">Create Income</h1>

    <form @submit.prevent="createIncome" class="form-content">
      <div class="form-grid">
        <div class="form-group">
          <label class="form-label">Category <span class="text-danger">*</span></label>
          <select v-model="form.category" class="form-select" required>
            <option value="" disabled>Select category...</option>
            <option v-for="option in categories" :key="option.value" :value="option.value">
              {{ option.label }}
            </option>
          </select>
        </div>

        <div class="form-group">
          <label class="form-label">Batch <span class="text-danger">*</span></label>
          <select v-model="form.batch" class="form-select" required>
            <option value="" disabled>Select batch...</option>
            <option v-for="batch in batches" :key="batch.slug" :value="batch.slug">
              {{ batch.name || batch.slug }}
            </option>
          </select>
        </div>

        <div class="form-group full-width">
          <label class="form-label">Description</label>
          <textarea
            v-model="form.description"
            class="form-control"
            rows="4"
            placeholder="Income details..."
          ></textarea>
        </div>

        <div class="form-group">
          <label class="form-label">Amount <span class="text-danger">*</span></label>
          <input
            type="number"
            v-model="form.amount"
            class="form-control"
            min="0.01"
            step="0.01"
            required
            placeholder="0.00"
          />
        </div>

        <div class="form-group">
          <label class="form-label">Date <span class="text-danger">*</span></label>
          <input
            type="date"
            v-model="form.date"
            class="form-control"
            required
          />
        </div>

        <div class="form-group">
          <label class="form-label">Currency <span class="text-danger">*</span></label>
          <select v-model="form.currency" class="form-select" required>
            <option value="€">Euros (€)</option>
            <option value="$">Dollars ($)</option>
            <option value="">Other</option>
          </select>
        </div>
      </div>

      <div class="form-actions">
        <button type="button" class="btn btn-secondary" @click="$router.back()">
          Cancel
        </button>
        <button type="submit" class="btn btn-success">
          Create Income
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