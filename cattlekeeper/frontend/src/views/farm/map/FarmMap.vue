<template>
  <div class="farm-container">
    <h2 class="farm-title">🐄 Vista general de las zonas de la granja</h2>

    <div ref="map" class="farm-map">
      <ZoneItem
        v-for="zone in zones"
        :key="zone.id"
        :zone="zone"
        @openDetails="showDetails"
      />

      <ZoneDetailsModal
        v-if="selectedZone"
        :zone="selectedZone"
        @close="selectedZone = null"
      />
    </div>
  </div>
</template>

  
  <script setup>
  import { ref, reactive } from 'vue';
  import ZoneItem from '@/components/farm/ZoneItem.vue';
  import ZoneDetailsModal from '@/components/farm/ZoneDetailsModal.vue';
  
  const selectedZone = ref(null);
  
  function showDetails(zone) {
  if (zone && typeof zone === 'object') {
    selectedZone.value = { ...zone };
  }}

  
  const zones = reactive([
    {
      id: 1,
      name: 'Potrero Sur',
      lot: 122,
      cattleCount: 62,
      entryDate: '03/08/2023',
      image: '/assets/Establo_icono.webp',
      animalImage: '/assets/vaca.png',
      x: 100,
      y: 200,
    },
    {
      id: 2,
      name: 'Gallinero Noroeste',
      lot: 45,
      cattleCount: 15,
      entryDate: '01/02/2024',
      image: '/assets/corral.png',
      animalImage: '/assets/gallina.png',
      x: 300,
      y: 200,
    },
    {
      id: 3,
      name: 'Potrero Sur',
      lot: 122,
      cattleCount: 62,
      entryDate: '03/08/2023',
      image: '/assets/Establo_icono.webp',
      animalImage: '/assets/vaca.png',
      x: 500,
      y: 200,
    },
    {
      id: 4,
      name: 'Potrero Sur',
      lot: 122,
      cattleCount: 62,
      entryDate: '03/08/2023',
      image: '/assets/Establo_icono.webp',
      animalImage: '/assets/vaca.png',
      x: 100,
      y: 300,
    },
  ]);
  
  const map = ref(null);
  let scale = 1;
  
  function handleZoom(e) {
    e.preventDefault();
    const delta = e.deltaY > 0 ? -0.1 : 0.1;
    scale += delta;
    scale = Math.min(Math.max(0.5, scale), 2);
    map.value.style.transform = `scale(${scale})`;
  }
  </script>
  
  <style scoped>
 .farm-container {
  max-width: 1200px;
  margin: 40px auto;
  padding: 24px;
  background: #ffffffee;
  border-radius: 16px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  text-align: center;
}

.farm-title {
  font-size: 28px;
  margin-bottom: 20px;
  color: #2e4e1d;
  font-weight: 600;
}

.farm-map {
  position: relative;
  width: 1100px;
  height: 600px;
  margin: 0 auto;
  background-image: url('/assets/establo-fondo.jpg');
  background-size: cover;
  background-position: center;
  background-color: #d5f2cc;
  overflow: hidden;
  border: 3px solid #b4cc9c;
  border-radius: 12px;
  transition: box-shadow 0.3s ease;
}

.farm-map:hover {
  box-shadow: 0 0 20px rgba(128, 128, 128, 0.3);
}
  </style>
  