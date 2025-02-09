<template>
    <div class="container mt-4">
      <h1 class="text-center">{{ t('order_details') }}</h1>
      <div v-if="order">
        <h4>Order #{{  order.id }}</h4>
        <h4>{{ t('order_date') }}: {{ formatDate(order.createdAt) }}</h4>
  
        <h3 class="mt-4">{{ t('products') }}</h3>
        <div class="row">
          <div v-for="product in order.items" :key="product.id" class="col-md-3 mb-4">
            <div class="card">
              <img :src="product.image" class="card-img-top" alt="Imagen de {{ product.name }}">
              <div class="card-body">
                <h5 class="card-title">{{ product.name }}</h5>
                <p class="card-text">Precio: {{ product.price }} €</p>
                <p class="card-text">Cantidad: {{ product.quantity }}</p>
              </div>
            </div>
          </div>
        </div>
  
        <h4 class="text-end">{{ t('total') }}: {{ order.totalPrice }} €</h4>
      </div>
      <div v-else>
        <p>{{t('not_found')}}</p>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import { useOrderStore } from '../stores/orderStore';
  import { useI18n } from 'vue-i18n';
  import { useRoute } from 'vue-router'; 
  
  const { t } = useI18n();
  const orderStore = useOrderStore();
  const route = useRoute(); 
  const orderId = ref<number | null>(null);
  const order = ref<any>(null); 
  
  onMounted(() => {
  orderId.value = Number(route.params.id);
  if (orderId.value) {
    order.value = orderStore.get_order(orderId.value);
    if (!order.value) {
      console.error('No se encontró el pedido con el ID:', orderId.value);
    }
  }
});
  const formatDate = (date: Date) => {
  const options: Intl.DateTimeFormatOptions = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };
  return new Date(date).toLocaleString('en-US', options);
};
  </script>
  
  <style scoped>
  .card-img-top {
    width: 100px; 
    height: 100px;
    object-fit: cover; 
    margin: 0 auto; 
  }
  </style>