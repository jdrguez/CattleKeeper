<script setup>
import { onMounted, ref } from 'vue';
import api from '@/api/axios';
import { useRouter } from 'vue-router';
import { useToast } from 'vue-toastification';

const toast = useToast();
const incomes = ref([]);
const router = useRouter();
const summary = ref([]);
const selectedCategory = ref('');
const selectedBatch = ref('');
const batchList = ref([]); 

const fetchBatches = async () => {
  try {
    const response = await api.get('api/farm/batch/');
    batchList.value = response.data; 
  } catch (error) {
  }
};

const fetchIncomes = async () => {
  try {
    const response = await api.get('api/farm/finances/incomes/', {
      params: {
        category: selectedCategory.value,
        batch: selectedBatch.value,
      },
    });
    incomes.value = response.data;
  } catch (error) {
    if (error.response && error.response.status === 402) {
      router.push('/plans');
    } else {
    }
  }
};

const deleteIncome = async (id) => {
  if (!confirm('Are you sure you want to delete this income?')) return;

  try {
    await api.delete(`api/farm/finances/incomes/${id}/delete/`);
    incomes.value = incomes.value.filter(i => i.id !== id);
    toast.success('Income deleted successfully.');
  } catch (error) {
    toast.error('Error deleting income');
  }
};
const getIncomesSummary = async () => {
  try {
    const response = await api.get('api/farm/finances/incomes/summary/');
    summary.value = response.data.summary;
  } catch (error) {
  }
};

onMounted(() => {
  fetchIncomes();
  getIncomesSummary();
  fetchBatches();
});
</script>

<template>
  <div class="page-container">
    <h1 class="page-title">Income List</h1>

    <section class="controls">
    <label for="category" class="label">Category</label>
  <select id="category" v-model="selectedCategory" @change="fetchIncomes" class="select">
    <option value="">All</option>
    <option value="SALE">Sale</option>
    <option value="SUBSIDY">Subsidy</option>
    <option value="DONATION">Donation</option>
    <option value="OTHER">Other</option>
  </select>

  <label for="batch" class="label"> Batch</label>
    <select id="batch" v-model="selectedBatch" @change="fetchIncomes" class="select">
      <option value="">All</option>
      <option v-for="batch in batchList" :key="batch.slug" :value="batch.slug">
        {{ batch.name || batch.slug }}
      </option>
    </select>

      <router-link :to="{ name: 'create-income' }" class="btn-link">
        <button class="btn-create"> New Income</button>
      </router-link>
    </section>

    <ul v-if="incomes.length" class="income-list">
      <li v-for="income in incomes" :key="income.id" class="income-item">
        <div class="income-content">
          <div class="income-main">
            <span class="income-category">{{ income.category }}</span>
            <span class="income-batch">{{ income.batch?.name || income.batch?.slug || '—' }}</span>
            <span class="income-amount">{{ income.amount }} {{ income.currency }}</span>
            <span class="income-date">{{ income.date }}</span>
          </div>
          <p v-if="income.description" class="income-desc"><i class="bi bi-card-text"></i> {{ income.description }}</p>
        </div>
        <div class="income-actions">
          <button @click="deleteIncome(income.id)" class="btn-delete"><i class="bi bi-trash"></i> Delete</button>
        </div>
      </li>
    </ul>

    <p v-else class="no-incomes">No registered income.</p>

    <section v-if="summary.length" class="summary-section">
      <h2 class="summary-title">Income Summary</h2>
      <ul class="summary-list">
        <li v-for="item in summary" :key="item.category" class="summary-item">
          <span class="summary-category">{{ item.category }}:</span>
          <span class="summary-total">{{ item.total }} {{ item.currency }}</span>
        </li>
      </ul>
    </section>
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

.controls {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem 1rem;
  margin-bottom: 2rem;
}

.label {
  flex-shrink: 0;
  font-weight: 600;
  color: #555;
  user-select: none;
}

.select {
  flex-grow: 1;
  padding: 0.5rem 1rem;
  font-size: 1rem;
  border-radius: 12px;
  border: 2px solid #cbd5e1;
  background: #f9fafb;
  transition: border-color 0.3s ease;
}

.select:focus {
  outline: none;
  border-color: #28a745;;
  box-shadow: 0 0 8px #33d459;
}

.btn-link {
  flex-shrink: 0;
}

.btn-create {
  padding: 0.55rem 1.6rem;
  background: linear-gradient(135deg, #28a745, #1e7e34);
  color: white;
  font-weight: 700;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  user-select: none;
  box-shadow: 0 6px 16px rgba(30, 126, 52, 0.5);
  transition: background 0.4s ease, box-shadow 0.4s ease;
}

.btn-create:hover,
.btn-create:focus {
  background: linear-gradient(135deg, #1e7e34, #28a745);
  box-shadow: 0 8px 24px rgba(30, 126, 52, 0.8);
  outline: none;
}

.income-list {
  list-style: none;
  padding: 0;
  margin: 0 0 2rem 0;
}

.income-item {
  background: #f6f9f6;
  padding: 1rem 1.4rem;
  margin-bottom: 1.2rem;
  border-radius: 14px;
  box-shadow:
    inset 2px 2px 6px #d9eedd,
    inset -2px -2px 6px #ffffff;
  transition: box-shadow 0.3s ease;
}

.income-item:hover {
  box-shadow:
    0 6px 18px rgba(40, 167, 69, 0.2);
}

.income-main {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem 2rem;
  font-weight: 600;
  font-size: 1.05rem;
  color: #2f4f2f;
  user-select: none;
}

.income-category {
  background: #28a745;
  color: #fff;
  padding: 0.15rem 0.9rem;
  border-radius: 14px;
  font-size: 0.9rem;
  user-select: none;
}

.income-batch,
.income-amount,
.income-date {
  user-select: none;
}

.income-desc {
  margin-top: 0.5rem;
  font-style: italic;
  color: #4c774c;
  user-select: text;
}


.income-actions {
  margin-top: 1rem;
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
}

.btn-delete {
  font-weight: 700;
  padding: 0.4rem 0.8rem;
  border-radius: 14px;
  cursor: pointer;
  border: none;
  user-select: none;
  font-size: 1rem;
  transition: background-color 0.25s ease;
}



.btn-delete {
  background: #fef0f0;
  color: #e74c3c;
}

.btn-delete:hover {
  background: #f9c6c3;
}

.no-incomes {
  font-style: italic;
  color: #95a5a6;
  user-select: none;
  text-align: center;
  margin-top: 3rem;
}

.summary-section {
  border-top: 2px solid #d4edda;
  padding-top: 1.8rem;
}

.summary-title {
  font-weight: 700;
  font-size: 1.6rem;
  margin-bottom: 1rem;
  color: #2f4f2f;
  user-select: none;
}

.summary-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 1rem 3rem;
}

.summary-item {
  background: #d4edda;
  padding: 0.6rem 1.4rem;
  border-radius: 14px;
  font-weight: 600;
  color: #2d3a45;
  user-select: none;
  box-shadow:
    inset 1px 1px 4px #b7d7b7,
    inset -1px -1px 4px #ffffff;
  flex: 1 1 180px;
  display: flex;
  justify-content: space-between;
}

.summary-category {
  color: #28a745;
}

.summary-total {
  font-weight: 700;
}
</style>
