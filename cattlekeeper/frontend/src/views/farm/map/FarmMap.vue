<template>
  <div class="farm-container">
    <h2 class="farm-title">Overview of the farm areas</h2>

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
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import ZoneItem from '@/components/farm/ZoneItem.vue';
import ZoneDetailsModal from '@/components/farm/ZoneDetailsModal.vue';
import api from '@/api/axios';

const router = useRouter();
const map = ref(null);
const scale = ref(1);
const selectedZone = ref(null);
const zones = ref([]);

function showDetails(zone) {
  if (zone && typeof zone === 'object') {
    selectedZone.value = { ...zone };
  }
}

function handleZoom(e) {
  e.preventDefault();
  const delta = e.deltaY > 0 ? -0.1 : 0.1;
  scale.value += delta;
  scale.value = Math.min(Math.max(0.5, scale.value), 2);
  if (map.value) {
    map.value.style.transform = `scale(${scale.value})`;
  }
}

onMounted(async () => {
  try {
    const response = await api.get('api/farm/batch/');
    const batches = response.data;

    zones.value = batches.map((batch, index) => ({
      id: batch.id || index,
      name: batch.name,
      species: batch.species,
      sex: batch.sex,
      cattleCount: batch.quantity,
      entryDate: batch.purchase_date || 'Sin fecha',
      image: getZoneImage(batch.species),
      animalImage: getAnimalImage(batch.species),
      x: getXPosition(index),
      y: getYPosition(index),
    }));
  } catch (error) {
    console.error('Error fetching batches:', error);
  }
});

const goToDetail = (slug) => {
  router.push({ name: 'BatchDetail', params: { batch_slug: slug } });
};

function getXPosition(index) {
  return 100 + (index % 4) * 250;
}

function getYPosition(index) {
  return 200 + Math.floor(index / 4) * 150;
}

function getZoneImage(species) {
  switch (species) {
    case 'Cattle': return '/assets/Establo_icono.webp'; 
    case 'Poultry': return '/assets/corral.png';        
    case 'Pig': return '/assets/lodo.png';  
    case 'Sheep': return '/assets/Establo_icono.webp';    
    case 'Goat': return '/assets/Establo_icono.webp';  
    default: return '/assets/Establo_icono.webp';  
  }
}

function getAnimalImage(species) {
  switch (species) {
    case 'Cattle': return '/assets/vaca.png';       
    case 'Poultry': return '/assets/gallina.png';   
    case 'Pig': return '/assets/pig.png';      
    case 'Sheep': return '/assets/sheep.png';      
    case 'Goat': return '/assets/goat.png';      
    default: return '/assets/vaca.png';
  }
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