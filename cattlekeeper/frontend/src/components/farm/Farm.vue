<template>
    <div ref="container" class="establo-container"></div>
  </template>
  
  <script setup>
  import { onMounted, ref } from 'vue'
  import Konva from 'konva'
  
  const container = ref(null)
  
  function loadImage(src) {
    return new Promise((resolve, reject) => {
      const img = new Image()
      img.onload = () => resolve(img)
      img.onerror = reject
      img.src = src
    })
  }
  
  onMounted(async () => {
    const width = 800
    const height = 500
    const cantidadVacas = 10
  
    const stage = new Konva.Stage({
      container: container.value,
      width,
      height,
    })
  
    const layer = new Konva.Layer()
    stage.add(layer)
  
    try {
      const fondo = await loadImage('/assets/establo-fondo.jpg')
      const vacaImg = await loadImage('/assets/vaca.png')
  
      const bg = new Konva.Image({
        x: 0,
        y: 0,
        image: fondo,
        width,
        height,
      })
      layer.add(bg)
  
      const vacas = []
      for (let i = 0; i < cantidadVacas; i++) {
        const vaca = new Konva.Image({
          x: 120 + Math.random() * 560,
          y: 120 + Math.random() * 260,
          image: vacaImg,
          width: 104,
          height: 104,
        })
        vacas.push(vaca)
        layer.add(vaca)
      }
  
      function moverVacas() {
        vacas.forEach(vaca => {
          const dx = (Math.random() - 0.5) * 4
          const dy = (Math.random() - 0.5) * 4
          const newX = vaca.x() + dx
          const newY = vaca.y() + dy
          if (newX > 0 && newX < width - 32 && newY > 100 && newY < height - 32) {
            vaca.x(newX)
            vaca.y(newY)
          }
        })
        layer.batchDraw()
      }
  
      setInterval(moverVacas, 100)
    } catch (err) {
      console.error('Error cargando imágenes:', err)
    }
  })
  </script>
  
  <style scoped>
  .establo-container {
    margin: 20px auto;
    width: 800px;
    height: 500px;
    border: 2px solid #444;
    background: #222;
  }
  </style>
  