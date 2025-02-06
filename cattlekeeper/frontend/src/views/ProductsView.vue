<template>
  <div>
    <h1>Products</h1>
    <div class="product-list">
      <div v-for="product in products" :key="product.id" class="product-item">
        <h2>{{ product.name }}</h2>
        <button @click="addToCart(product)">Add to Cart</button>
      </div>
    </div>
    <h2>Shopping Cart ({{ cartTotal }})</h2>
    <div v-if="cartItems.length">
      <ul>
        <li v-for="item in cartItems" :key="item.id">
          {{ item.name }} - Quantity: {{ item.quantity }}
        </li>
      </ul>
    </div>
    <div v-else>
      <p>Your cart is empty.</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { useCartStore } from '../stores/cartStore';

const cartStore = useCartStore();
const products = ref([
  { id: 1, name: 'Product 1' },
  { id: 2, name: 'Product 2' },
  { id: 3, name: 'Product 3' },
]);

const addToCart = (product: { id: number; name: string }) => {
  cartStore.addItem({ id: product.id, name: product.name, quantity: 1 });
};

const cartItems = computed(() => cartStore.items);
const cartTotal = computed(() => cartStore.getTotalItems());
</script>

<style scoped>
.product-list {
  display: flex;
  flex-direction: column;
}

.product-item {
  margin: 10px 0;
}
</style>
