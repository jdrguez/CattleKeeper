<template>
  <div>
    <div ref="chartContainer" style="width: 100%; height: 400px;"></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import * as echarts from 'echarts'
import api from '@/api/axios'

const chartContainer = ref(null)

const loadData = async () => {
  try {
    const res = await api.get('/api/stats/batch-net-income/')
    const data = res.data.batches

    const batches = data.map(d => d.batch)
    const income = data.map(d => d.income)
    const expense = data.map(d => d.expense)
    const net = data.map(d => d.net)

    const chart = echarts.init(chartContainer.value)

    chart.setOption({
      title: { text: 'Ingreso Neto por Lote', left: 'center' },
      tooltip: { trigger: 'axis' },
      legend: { data: ['Ingreso', 'Gasto', 'Neto'], top: 30 },
      xAxis: { type: 'category', data: batches },
      yAxis: { type: 'value' },
      series: [
        { name: 'Ingreso', type: 'bar', data: income, itemStyle: { color: '#4caf50' } },
        { name: 'Gasto', type: 'bar', data: expense, itemStyle: { color: '#f44336' } },
        { name: 'Neto', type: 'line', data: net, itemStyle: { color: '#2196f3' } }
      ]
    })
  } catch (err) {
    console.error('Error al cargar lotes:', err)
  }
}

onMounted(loadData)
</script>
