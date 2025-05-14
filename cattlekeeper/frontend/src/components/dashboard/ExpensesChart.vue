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
    const res = await axios.get('http://localhost:8000/api/stats/expense-category-summary/')
    const data = res.data.category_summary

    const chart = echarts.init(chartContainer.value)

    chart.setOption({
      title: { text: 'Gastos por Categoría', left: 'center' },
      tooltip: { trigger: 'item' },
      series: [
        {
          type: 'pie',
          radius: '60%',
          data: data.map(item => ({
            name: item.category,
            value: item.total
          }))
        }
      ]
    })
  } catch (err) {
    console.error('Error al cargar gastos:', err)
  }
}

onMounted(loadData)
</script>
