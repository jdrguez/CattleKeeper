<template>
<div class="container mt-4">
    <h1 class="text-center">{{ t('products') }}</h1>
    <div class="row">
        <div v-for="product in products" :key="product.id" class="col-md-3 mb-4">
            <div class="card">
                <img :src="getFullImageUrl(product.image)" class="card-img-top" alt="Imagen de {{ product.name }}">
                <div class="card-body">
                    <h5 class="card-title">{{ product.name }}</h5>
                    <p class="card-text">Precio: {{ product.price }} €</p>
                    <button @click="addToCart(product)" class="btn btn-primary me-2">
                      <i class="bi bi-cart2"></i>
                    </button>
                    <button @click="addWish(product)" class="btn btn-primary">
                        <i class="bi bi-heart-fill"></i>
                    </button> 
                </div>
            </div>
        </div>
    </div>
</div>
    <h2 class="mt-4">{{ t('cart')}} ({{ cartTotal }})</h2>
    <div v-if="cartItems.length">
      <ul class="list-group mb-4">
        <li v-for="item in cartItems" :key="item.id" class="list-group-item d-flex justify-content-between align-items-center">
            <div>
                <strong>{{ item.name }}</strong> - items: {{ item.quantity }}
            </div>
            <span class="badge bg-primary rounded-pill">{{ cartStore.get_price(item) }} €</span>
        </li>
    </ul>
    <h4 class="text-end">Total: {{ cartPrice }} €</h4>
    <button @click="placeOrder" class="btn btn-success">{{t('checkout')}}</button>
</div>
    <div v-else>
      <p>{{t('empty_cart')}}</p>
    </div>
  
</template>

<script setup lang="ts">
import { defineComponent, ref, computed, onMounted } from 'vue';
import { useCartStore } from '../../../stores/cartStore';
import { useOrderStore } from '../../../stores/orderStore';
import { useWishlistStore } from '../../../stores/wishlistStore';
import { useI18n } from 'vue-i18n';
import api from '@/api/axios.ts'

const { t } = useI18n();
const cartStore = useCartStore();
const orderStore = useOrderStore();
const wishlistStore = useWishlistStore();

const backendUrl = 'http://127.0.0.1:8000'  

const getFullImageUrl = (path:any) => {
  return backendUrl + path
}

function placeOrder() {
  const totalPrice = cartStore.getTotalPrice();
  orderStore.addOrder(cartStore.items, parseFloat(totalPrice));
  alert('¡purchase added successfully!');
    cartStore.items = [];}


interface Product {
  id: number;
  name: string;
  price: number;
  image: string;
}

const products = ref<Product[]>([]);


api.get('/api/products/')
  .then(response => {
    const datos = response.data
    datos.forEach((element: { id: number, name: string, price: number, image: string }) => {
      products.value.push(element)
    })
  })
  .catch(error => {
    console.error('Hubo un error al obtener los productos:', error)

  })


const addToCart = (product: { id: number; name: string; price:number;}) => {
  cartStore.addItem({ id: product.id, name: product.name, quantity: 1, price: product.price });
};

const addWish = (product: { id: number; name: string; price:number;}) => {
  wishlistStore.addItem(product);
  alert('Added to your wishlist');
};

const cartItems = computed(() => cartStore.items);
const cartTotal = computed(() => cartStore.getTotalItems());
const cartPrice = computed(() => cartStore.getTotalPrice());


</script>

<style scoped>
.card-img-top {
    width: 100px; 
    height: 100px;
    object-fit: cover; 
    margin: 0 auto; 
}
</style>
