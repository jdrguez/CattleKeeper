<script setup>
import { onMounted, ref } from 'vue';
import api from '@/api/axios';
import { useRouter } from 'vue-router';

const incomes = ref([]);
const router = useRouter();
const summary = ref([]);

const fetchIncomes = async () => {
  try {
    const response = await api.get('api/farm/finances/incomes/');
    incomes.value = response.data;
  } catch (error) {
    console.error('Error al obtener ingresos:', error);
    alert('Hubo un error al obtener los ingresos.');
  }
};

const deleteIncome = async (id) => {
  if (!confirm('¿Estás seguro de que deseas eliminar este ingreso?')) return;

  try {
    await api.delete(`api/farm/finances/incomes/${id}/delete/`);
    incomes.value = incomes.value.filter(i => i.id !== id);
    alert('Ingreso eliminado.');
  } catch (error) {
    console.error('Error eliminando ingreso:', error);
    alert('No se pudo eliminar el ingreso.');
  }
};
const getIncomesSummary = async () => {
  try {
    const response = await api.get('api/farm/finances/incomes/summary/');
    summary.value = response.data.summary;
  } catch (error) {
    console.error('Error al obtener el resumen de gastos:', error);
  }
};

onMounted(() => {
  fetchIncomes(); 
  getIncomesSummary(); 
});

</script>

<template>
  <div>
    <h1>Ingresos</h1>
    <router-link :to="{ name: 'create-income' }">
      <button>➕ Nuevo Ingreso</button>
    </router-link>

    <table>
      <thead>
        <tr>
          <th>Categoría</th>
          <th>Lote</th>
          <th>Descripción</th>
          <th>Monto</th>
          <th>Fecha</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="income in incomes" :key="income.id">
          <td>{{ income.category }}</td>
          <td>{{ income.batch?.name || income.batch?.slug || '—' }}</td>
          <td>{{ income.description }}</td>
          <td>{{ income.amount }} {{ income.currency }}</td>
          <td>{{ income.date }}</td>
          <td>
            <router-link :to="{ name: 'edit-income', params: { id: income.id } }">
              <button>Editar</button>
            </router-link>
            <button @click="deleteIncome(income.id)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>
    <div v-if="summary.length">
      <h2>Resumen de Ingresos</h2>
      <ul>
        <li v-for="item in summary" :key="item.category">
          {{ item.category }}: {{ item.total }} {{ item.currency }}
        </li>
      </ul>
    </div>
  </div>
</template>
