<template>
    <div
      class="zone"
      :style="{ top: zone.y + 'px', left: zone.x + 'px' }"
      @mouseover="hovered = true"
      @mouseleave="hovered = false"
      @click="$emit('openDetails', zone)"
    >
      <img :src="zone.image" class="zone-image" />
      <img v-if="zone.animalImage" :src="zone.animalImage" class="animal" />
  
      <div v-if="hovered" class="zone-info">
        <strong>{{ zone.name }}</strong><br />
        Lote: {{ zone.lot }}<br />
        C. Ganado: {{ zone.cattleCount }}<br />
        Entrada: {{ zone.entryDate }}
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  defineProps(['zone']);
  defineEmits(['openDetails']);
  
  const hovered = ref(false);
  </script>
  
  <style scoped>
  .zone {
    position: absolute;
    cursor: pointer;
    transition: transform 0.2s;
  }
  .zone:hover {
    transform: scale(1.05);
  }
  .zone-image {
    width: 120px;
  }
  .animal {
    position: absolute;
    width: 40px;
    top: 60px;
    left: 40px;
    animation: bounce 1s infinite;
  }
  .zone-info {
    position: absolute;
    top: -90px;
    left: 0;
    background: #ffffffdd;
    border: 1px solid #ccc;
    padding: 6px;
    border-radius: 6px;
    font-size: 12px;
    width: 160px;
    z-index: 10;
  }
  @keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-5px); }
  }
  </style>
  