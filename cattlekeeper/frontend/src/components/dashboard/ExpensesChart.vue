<template>
  <div>
    <div ref="chartContainer" style="width: 100%; height: 400px;"></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import * as echarts from 'echarts'
import api from '@/api/axios'
import { useRouter } from 'vue-router'

const router = useRouter()

const chartContainer = ref(null)

const loadData = async () => {
  try {
    const res = await api.get('/api/stats/expense-category-summary/')
    const data = res.data.category_summary

    const chart = echarts.init(chartContainer.value)

    chart.setOption({
      title: { text: 'Expenses by Category', left: 'center' },
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
  } catch (error) {
    if (error.response && error.response.status== 402){
      router.push('/plans')
    }else{
      console.error('Error loading expenses:', error)
    }
  }
}

onMounted(loadData)
</script>
