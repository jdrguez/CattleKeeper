<template>
  <div>
    <div ref="chartContainer" style="width: 100%; height: 400px;"></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import * as echarts from 'echarts'
import axios from 'axios'

const chartContainer = ref(null)

const loadData = async () => {
  try {
    const res = await axios.get('http://localhost:8000/api/stats/production-summary/')
    const data = res.data.production_summary

    const chart = echarts.init(chartContainer.value)

    chart.setOption({
      title: { text: 'Producción por Tipo', left: 'center' },
      tooltip: { trigger: 'item' },
      series: [
        {
          type: 'pie',
          radius: '60%',
          data: data.map(item => ({
            name: item.production_type,
            value: item.total
          }))
        }
      ]
    })
  } catch (err) {
    console.error('Error al cargar producción:', err)
  }
}

onMounted(loadData)
</script>
