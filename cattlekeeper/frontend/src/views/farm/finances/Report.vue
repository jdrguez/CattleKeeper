<template>
    <div class="p-4">
  
      <h1 class="text-xl font-bold mb-4">Descargar Reporte PDF</h1>
      <button @click="getPdfReport" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
        Descargar PDF
      </button>
    </div>
  </template>
  
  <script setup>
  import api from '@/api/axios';
  import { useToast } from 'vue-toastification';
  import Breadcrumbs from '@/components/utils/Breadcrumbs.vue';
  
  const toast = useToast();
  
  const getPdfReport = async () => {
    try {
      const response = await api.get('api/stats/report/pdf/', {
        responseType: 'blob'
      });
  
      const blob = new Blob([response.data], { type: 'application/pdf' });
      const url = window.URL.createObjectURL(blob);
  
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'reporte.pdf');
      document.body.appendChild(link);
      link.click();
      link.remove();
      window.URL.revokeObjectURL(url);
  
      toast.success('Reporte descargado correctamente');
    } catch(error) {
      if (error.response && error.response.status== 402){
        router.push('/plans')
      }else{
        console.error('Error al descargar el PDF:', error);
        toast.error('No se pudo descargar el reporte. ¿Estás autenticado?');
      }
     
    }
  };
  </script>
  