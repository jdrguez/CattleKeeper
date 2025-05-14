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
let chartInstance = null

const drawChart = (months, income, expense, net) => {
  if (!chartContainer.value) return

  chartInstance = echarts.init(chartContainer.value)

  const options = {
    title: {
      text: 'Ingresos vs Gastos Mensuales',
      left: 'center'
    },
    tooltip: {
      trigger: 'axis'
    },
    legend: {
      data: ['Ingresos', 'Gastos', 'Neto'],
      top: 30
    },
    xAxis: {
      type: 'category',
      data: months
    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        name: 'Ingresos',
        type: 'bar',
        data: income,
        itemStyle: { color: '#4caf50' }
      },
      {
        name: 'Gastos',
        type: 'bar',
        data: expense,
        itemStyle: { color: '#f44336' }
      },
      {
        name: 'Neto',
        type: 'line',
        data: net,
        itemStyle: { color: '#2196f3' }
      }
    ]
  }

  chartInstance.setOption(options)
}

const loadData = async () => {
  try {
    const res = await axios.get('http://localhost:8000/api/stats/monthly-summary/')
    const summary = res.data?.monthly_summary ?? []

    if (summary.length === 0) {
      console.warn('No hay datos para mostrar.')
      return
    }

    const months = summary.map(s => `${s.month}`.padStart(2, '0'))
    const income = summary.map(s => s.income)
    const expense = summary.map(s => s.expense)
    const net = summary.map(s => s.net)

    drawChart(months, income, expense, net)
  } catch (err) {
    console.error('Error al obtener datos del backend:', err)
  }
}

onMounted(loadData)
</script>

<style scoped>
/* puedes agregar más estilos aquí si necesitas */
</style>
