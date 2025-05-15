<template>
  <div class="page-container">
    <h1 class="page-title">Listado de Gastos</h1>

    <section class="controls">
      <label for="category" class="label">Categoría</label>
      <select id="category" v-model="selectedCategory" @change="getExpenses" class="select">
        <option value="">Todas</option>
        <option value="FEED">Alimento</option>
        <option value="VET">Veterinaria</option>
        <option value="MAINTENANCE">Mantenimiento</option>
        <option value="LABOR">Mano de obra</option>
        <option value="EQUIPMENT">Equipamiento</option>
        <option value="OTHER">Otro</option>
      </select>

      <router-link :to="{ name: 'expense-create' }" class="btn-link">
        <button class="btn-create">➕ Crear Gasto</button>
      </router-link>
    </section>

    <ul v-if="expenses.length" class="expense-list">
      <li v-for="expense in expenses" :key="expense.id" class="expense-item">
        <div class="expense-main">
          <span class="expense-category">{{ expense.category }}</span>
          <span class="expense-batch">{{ expense.batch.name }}</span>
          <span class="expense-amount">{{ expense.amount }} {{ expense.currency }}</span>
          <span class="expense-date">{{ expense.date }}</span>
        </div>
        <p v-if="expense.description" class="expense-desc">📝 {{ expense.description }}</p>

        <div class="expense-actions">
          <router-link :to="{ name: 'expense-update', params: { expense_pk: expense.id } }" class="btn-edit">✏️ Editar</router-link>
          <button @click="deleteExpense(expense.id)" class="btn-delete">🗑️ Eliminar</button>
        </div>
      </li>
    </ul>

    <p v-else class="no-expenses">No hay gastos registrados.</p>

    <section v-if="summary.length" class="summary-section">
      <h2 class="summary-title">Resumen de Gastos</h2>
      <ul class="summary-list">
        <li v-for="item in summary" :key="item.category" class="summary-item">
          <span class="summary-category">{{ item.category }}:</span>
          <span class="summary-total">{{ item.total }} {{ item.currency }}</span>
        </li>
      </ul>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import api from '@/api/axios';

const route = useRoute();
const batchSlug = route.params.batch_slug; 
const expenses = ref([]);
const summary = ref([]);
const selectedCategory = ref('');
const selectedBatch = ref(batchSlug);

const getExpenses = async () => {
  try {
    const response = await api.get('api/farm/finances/expenses/', {
      params: {
        category: selectedCategory.value,
        batch: selectedBatch.value,
      },
    });
    expenses.value = response.data;
  } catch (error) {
    console.error('Error al obtener los gastos:', error);
  }
};

const getExpenseSummary = async () => {
  try {
    const response = await api.get('api/farm/finances/expenses/summary/');
    summary.value = response.data.summary;
  } catch (error) {
    console.error('Error al obtener el resumen de gastos:', error);
  }
};

const deleteExpense = async (id) => {
  try {
    await api.delete(`api/farm/finances/expenses/${id}/delete/`);
    expenses.value = expenses.value.filter(e => e.id !== id);
    alert('Gasto eliminado con éxito');
  } catch (error) {
    alert('Error al eliminar gasto');
    console.error(error);
  }
};

onMounted(() => {
  getExpenses();
  getExpenseSummary();
});
</script>

<style scoped>
.page-container {
  max-width: 720px;
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
  border-bottom: 3px solid #4a90e2;
  padding-bottom: 0.3rem;
  margin-bottom: 1.8rem;
  letter-spacing: 0.03em;
  user-select: none;
}

.controls {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2rem;
}

.label {
  flex-shrink: 0;
  font-weight: 600;
  color: #555;
  min-width: 100px;
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
  border-color: #4a90e2;
  box-shadow: 0 0 8px #4a90e2aa;
}

.btn-link {
  flex-shrink: 0;
}

.btn-create {
  padding: 0.55rem 1.6rem;
  background: linear-gradient(135deg, #4a90e2, #357abd);
  color: white;
  font-weight: 700;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  user-select: none;
  box-shadow: 0 6px 16px rgba(53, 122, 189, 0.5);
  transition: background 0.4s ease, box-shadow 0.4s ease;
}

.btn-create:hover,
.btn-create:focus {
  background: linear-gradient(135deg, #357abd, #4a90e2);
  box-shadow: 0 8px 24px rgba(53, 122, 189, 0.8);
  outline: none;
}

.expense-list {
  list-style: none;
  padding: 0;
  margin: 0 0 2rem 0;
}

.expense-item {
  background: #f6f9fc;
  padding: 1rem 1.4rem;
  margin-bottom: 1.2rem;
  border-radius: 14px;
  box-shadow:
    inset 2px 2px 6px #d9e6f0,
    inset -2px -2px 6px #ffffff;
  transition: box-shadow 0.3s ease;
}

.expense-item:hover {
  box-shadow:
    0 6px 18px rgba(74, 144, 226, 0.2);
}

.expense-main {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem 2rem;
  font-weight: 600;
  font-size: 1.05rem;
  color: #34495e;
  user-select: none;
}

.expense-category {
  background: #4a90e2;
  color: #fff;
  padding: 0.15rem 0.9rem;
  border-radius: 14px;
  font-size: 0.9rem;
  user-select: none;
}

.expense-batch,
.expense-amount,
.expense-date {
  user-select: none;
}

.expense-desc {
  margin-top: 0.5rem;
  font-style: italic;
  color: #66788a;
  user-select: text;
}

.expense-actions {
  margin-top: 1rem;
  display: flex;
  gap: 1rem;
}

.btn-edit,
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

.btn-edit {
  background: #ebf2ff;
  color: #357abd;
}

.btn-edit:hover {
  background: #c5d8ff;
}

.btn-delete {
  background: #ffeded;
  color: #e74c3c;
}

.btn-delete:hover {
  background: #f9c6c3;
}

.no-expenses {
  font-style: italic;
  color: #95a5a6;
  user-select: none;
  text-align: center;
  margin-top: 3rem;
}

.summary-section {
  border-top: 2px solid #e2e8f0;
  padding-top: 1.8rem;
}

.summary-title {
  font-weight: 700;
  font-size: 1.6rem;
  margin-bottom: 1rem;
  color: #34495e;
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
  background: #e8f0fe;
  padding: 0.6rem 1.4rem;
  border-radius: 14px;
  font-weight: 600;
  color: #2d3a45;
  user-select: none;
  box-shadow:
    inset 1px 1px 4px #c6d0e9,
    inset -1px -1px 4px #ffffff;
  flex: 1 1 180px;
  display: flex;
  justify-content: space-between;
}

.summary-category {
  color: #4a90e2;
}

.summary-total {
  font-weight: 700;
}
</style>
