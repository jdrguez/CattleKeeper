<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import api from '@/api/axios';

const route = useRoute();
const router = useRouter();
const expensePk = route.params.expense_pk;
const form = ref({
  category: '',
  batch: '',
  description: '',
  amount: '',
  payment_method: '',
  date: '',
  currency: '€',
});

const categories = [
  { value: 'FEED', label: 'Alimento' },
  { value: 'VET', label: 'Veterinaria' },
  { value: 'MAINTENANCE', label: 'Mantenimiento' },
  { value: 'LABOR', label: 'Mano de obra' },
  { value: 'EQUIPMENT', label: 'Equipamiento' },
  { value: 'OTHER', label: 'Otro' }
];

const paymentMethods = [
  { value: 'CASH', label: 'Efectivo' },
  { value: 'BANK_TRANSFER', label: 'Transferencia Bancaria' },
  { value: 'MOBILE_PAYMENT', label: 'Pago Móvil' },
  { value: 'CHECK', label: 'Cheque' },
  { value: 'OTHER', label: 'Otro' }
];

onMounted(async () => {
  try {
    const response = await api.get(`api/finances/expenses/${expensePk}/`);
    const expense = response.data;
    form.value = { ...expense }; 
  } catch (error) {
    console.error('Error cargando gasto:', error);
  }
});

const updateExpense = async () => {
  try {
    await api.post(`api/farm/finances/expenses/${expensePk}/update/`, form.value);
    alert('Gasto actualizado correctamente');
    router.push({ name: 'expenses' });
  } catch (error) {
    console.error('Error actualizando gasto:', error);
    alert('Hubo un error al actualizar el gasto.');
  }
};
</script>

<template>
  <div>
    <h1>Actualizar Gasto</h1>
    <form @submit.prevent="updateExpense">
      <div>
        <label>Categoría:</label>
        <select v-model="form.category" required>
          <option v-for="option in categories" :key="option.value" :value="option.value">
            {{ option.label }}
          </option>
        </select>
      </div>

      <div>
        <label>Descripción:</label>
        <textarea v-model="form.description" required placeholder="Descripción"></textarea>
      </div>

      <div>
        <label>Monto:</label>
        <input v-model="form.amount" type="number" required placeholder="Monto" />
      </div>

      <div>
        <label>Método de Pago:</label>
        <select v-model="form.payment_method" required>
          <option v-for="option in paymentMethods" :key="option.value" :value="option.value">
            {{ option.label }}
          </option>
        </select>
      </div>

      <div>
        <label>Fecha:</label>
        <input v-model="form.date" type="date" required />
      </div>

      <div>
        <label>Moneda:</label>
        <select v-model="form.currency" required>
          <option value="€">Euros</option>
          <option value="$">Dólares</option>
          <option value="">Otro</option>
        </select>
      </div>

      <button type="submit">Actualizar Gasto</button>
    </form>
  </div>
</template>
