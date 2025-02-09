<template>
    <div class="container mt-4">
      <h1 class="text-center">{{ t('wishlist') }}</h1>
      <div v-if="wishlistItems.length > 0">
        <div class="row">
          <div v-for="item in wishlistItems" :key="item.id" class="col-md-3 mb-4">
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">{{ item.name }}</h5>
                <p class="card-text">Precio: {{ item.price }} €</p>
                <button @click="removeFromWishlist(item.id)" class="btn btn-danger">
                  {{ t('remove') }}
                </button>
              </div>
            </div>
          </div>
        </div>
        <h4 class="text-end">{{ t('total_items') }}: {{ wishlistCount }}</h4>
      </div>
      <div v-else>
        <p>{{ t('empty_wishlist') }}</p>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { computed } from 'vue';
  import { useWishlistStore } from '../stores/wishlistStore';
  import { useI18n } from 'vue-i18n';
  
  const { t } = useI18n();
  const wishlistStore = useWishlistStore();
  
  const wishlistItems = computed(() => wishlistStore.items);
  const wishlistCount = computed(() => wishlistStore.get_total());
  
  const removeFromWishlist = (itemId: number) => {
    wishlistStore.removeItem(itemId);
  };
  </script>
  
  <style scoped>
  .card {
    cursor: pointer;
  }
  </style>