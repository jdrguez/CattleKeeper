<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <h2 class="modal-title">{{ zone.name }}</h2>
      <div class="modal-details">
        <p><strong>Lote:</strong> {{ zone.lot }}</p>
        <p><strong>Ganado:</strong> {{ zone.cattleCount }}</p>
        <p><strong>Fecha de entrada:</strong> {{ zone.entryDate }}</p>
      </div>
      <button class="modal-close-btn" @click="$emit('close')">Cerrar</button>
    </div>
  </div>
</template>

<script setup>
defineProps({
  zone: {
    type: Object,
    required: true
  }
});
defineEmits(['close']);
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0; left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0,0,0,0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  backdrop-filter: blur(2px);
}

.modal-content {
  background: #fff;
  padding: 2rem;
  border-radius: 16px;
  width: 90%;
  max-width: 500px;
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.2);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  animation: fadeIn 0.1s ease-in-out;
  text-align: center;
}

.modal-title {
  font-size: 24px;
  color: #2e4e1d;
  margin-bottom: 1rem;
}

.modal-details p {
  font-size: 16px;
  color: #444;
  margin: 0.5rem 0;
}

.modal-close-btn {
  margin-top: 1.5rem;
  padding: 0.5rem 1.2rem;
  background-color: #2e4e1d;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.modal-close-btn:hover {
  background-color: #3c6a29;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
