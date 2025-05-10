<template>
  <div ref="chart" style="width: 100%; height: 400px;"></div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import * as echarts from 'echarts';
import api from '@/api/axios';

const chart = ref(null);
let myChart = null;
const source = ref([]);

const loadData = async () => {
  try {
    const response = await api.get('/api/animals');
    source.value = response.data;

    const numRows = source.value.length - 1; // excluye la fila de cabecera

    const option = {
      legend: {},
      tooltip: {},
      dataset: {
        source: source.value
      },
      xAxis: [
        { type: 'category', gridIndex: 0 }, // Eje X superior
        { type: 'category', gridIndex: 1 }  // Eje X inferior
      ],
      yAxis: [
        { gridIndex: 0 }, // Y superior
        { gridIndex: 1 }  // Y inferior
      ],
      grid: [
        { bottom: '55%' }, // Gráfico superior
        { top: '55%' }     // Gráfico inferior
      ],
      series: [
        // Series para la parte superior
        ...Array.from({ length: numRows }, () => ({
          type: 'bar',
          seriesLayoutBy: 'row'
        })),
        // Series para la parte inferior
        ...Array.from({ length: numRows }, () => ({
          type: 'bar',
          xAxisIndex: 1,
          yAxisIndex: 1
        }))
      ]
    };

    myChart.setOption(option);
  } catch (error) {
    console.error('Hubo un error al obtener los animales:', error);
  }
};

onMounted(() => {
  myChart = echarts.init(chart.value);
  loadData();
});

onBeforeUnmount(() => {
  if (myChart) {
    myChart.dispose();
  }
});
</script>

<style scoped>
</style>
