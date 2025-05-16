<template>
    <nav aria-label="breadcrumb" class="breadcrumb-container">
      <ol class="breadcrumb-list">
        <li v-for="(crumb, index) in breadcrumbs" :key="index" class="breadcrumb-item">
          <router-link v-if="index < breadcrumbs.length - 1" :to="crumb.to">
            {{ crumb.text }}
          </router-link>
          <span v-else>{{ crumb.text }}</span>
        </li>
      </ol>
    </nav>
  </template>
  
  <script setup>
  import { computed } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  
  const route = useRoute()
  const router = useRouter()
  
  function resolveBreadcrumbText(routeRecord, routeParams) {
    // Aquí personaliza textos dinámicos para rutas con params
    if (routeRecord.name === 'BatchDetail') {
      return `Lote ${routeParams.batch_slug}`
    }
    if (routeRecord.name === 'AnimalDetail') {
      return `Animal ${routeParams.animal_slug}`
    }
    if (routeRecord.name === 'ProductionEdit') {
      return `Editar producción #${routeParams.production_pk}`
    }
    // Añade más según necesites
    return routeRecord.meta.breadcrumb || routeRecord.name
  }
  
  const breadcrumbs = computed(() => {
    const matched = route.matched.filter(r => r.meta && r.meta.breadcrumb)
    return matched.map(r => ({
      text: resolveBreadcrumbText(r, route.params),
      to: { name: r.name, params: route.params },
    }))
  })
  console.log(breadcrumbs)
  </script>
  
  <style scoped>
  .breadcrumb-container {
    padding: 10px 0;
  }
  .breadcrumb-list {
    list-style: none;
    display: flex;
    gap: 0.5em;
  }
  .breadcrumb-item::after {
    content: '/';
    margin-left: 0.5em;
  }
  .breadcrumb-item:last-child::after {
    content: '';
  }
  </style>
  