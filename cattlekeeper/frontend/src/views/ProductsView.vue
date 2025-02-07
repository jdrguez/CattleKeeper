<template>
  <div class="container mt-4">
    <h1 class="text-center">Products</h1>
    <div class="row">
      <div v-for="product in products" :key="product.id" class="col-md-4 mb-4">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">{{ product.name }}</h5>
            <button @click="addToCart(product)" class="btn btn-primary">Añadir al carrito</button>
          </div>
        </div>
      </div>
    </div>
    <h2 class="mt-4">Carrito ({{ cartTotal }})</h2>
    <div v-if="cartItems.length">
      <ul class="list-group">
        <li v-for="item in cartItems" :key="item.id" class="list-group-item">
          {{ item.name }} - Cantidad: {{ item.quantity }}
        </li>
      </ul>
    </div>
    <div v-else>
      <p>Your cart is empty.</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { useCartStore } from '../stores/cartStore';

const cartStore = useCartStore();
interface Product {
  id: number;
  name: string;
}

const products = ref<Product[]>([]);

onMounted(() => {
  fetch('http://127.0.0.1:8000/api/products', {
    method: 'GET',
  })
  .then(respuesta => {
    if (!respuesta.ok) {
      throw new Error('Network response was not ok');
    }
    return respuesta.json();
  })
  .then(datos => {
    datos.forEach((element: {id : number, name : string}) => {
      products.value.push(element)
    });
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });
});

const addToCart = (product: { id: number; name: string }) => {
  cartStore.addItem({ id: product.id, name: product.name, quantity: 1 });
};

const cartItems = computed(() => cartStore.items);
const cartTotal = computed(() => cartStore.getTotalItems());
</script>

<style scoped>
</style>
