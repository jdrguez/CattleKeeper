<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import api from '@/api/axios';
import { useToast } from 'vue-toastification';

const router = useRouter();
const toast = useToast();

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

// Lotes cargados desde la API
const batches = ref([]);

const fetchBatches = async () => {
  try {
    const response = await api.get('api/farm/batch');
    batches.value = response.data;
  } catch (error) {
    console.error('Error al cargar lotes:', error);
  }
};

onMounted(() => {
  fetchBatches();
});

const createExpense = async () => {
  try {
    await api.post('api/farm/finances/expenses/create/', form.value);
    toast.success('Se ha creado un gasto correctamente')
    router.push({ name: 'expenses' });
  } catch (error) {
    console.error('Error creando gasto:', error);
    toast.error('No se ha creado el gasto')
  }
};
</script>

<template>
  <div>
    <h1>Crear Gasto</h1>
    <form @submit.prevent="createExpense">
      <div>
        <label>Categoría:</label>
        <select v-model="form.category" required>
          <option v-for="option in categories" :key="option.value" :value="option.value">
            {{ option.label }}
          </option>
        </select>
      </div>

      <div>
        <label>Lote:</label>
        <select v-model="form.batch" required>
          <option value="" disabled selected>Selecciona un lote</option>
          <option v-for="batch in batches" :key="batch.slug" :value="batch.slug">
            {{ batch.name || batch.slug }}
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

      <button type="submit">Crear Gasto</button>
    </form>
  </div>
</template>
