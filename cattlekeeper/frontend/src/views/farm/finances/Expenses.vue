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

<template>
  <div>
    <h1>Listado de Gastos</h1>

    <div>
      <label for="category">Categoría</label>
      <select v-model="selectedCategory" @change="getExpenses">
        <option value="">Todas</option>
        <option value="FEED">Alimento</option>
        <option value="VET">Veterinaria</option>
        <option value="MAINTENANCE">Mantenimiento</option>
        <option value="LABOR">Mano de obra</option>
        <option value="EQUIPMENT">Equipamiento</option>
        <option value="OTHER">Otro</option>
      </select>
    </div>
    <router-link :to="{ name: 'expense-create' }">
    <button>➕ Crear Gasto</button>
    </router-link>

    <ul v-if="expenses.length">
      <li v-for="expense in expenses" :key="expense.id">
        <strong>{{ expense.category }}:</strong> 
        {{ expense.batch.name }} - {{ expense.amount }} {{ expense.currency }} ({{ expense.date }})
        <div v-if="expense.description">📝 {{ expense.description }}</div>
        <router-link :to="{ name: 'expense-update', params: { expense_pk: expense.id } }">
            <button>✏️ Editar</button>
            </router-link>
            <button @click="deleteExpense(expense.id)">🗑️ Eliminar</button>

      </li>
    </ul>
    <p v-else>No hay gastos registrados.</p>

    <div v-if="summary.length">
      <h2>Resumen de Gastos</h2>
      <ul>
        <li v-for="item in summary" :key="item.category">
          {{ item.category }}: {{ item.total }} {{ item.currency }}
        </li>
      </ul>
    </div>
  </div>
</template>
