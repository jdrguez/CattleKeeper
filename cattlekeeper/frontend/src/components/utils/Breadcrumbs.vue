<template>
  <nav aria-label="breadcrumb" class="breadcrumb">
    <ol>
      <li
        v-for="(item, index) in breadcrumb"
        :key="index"
        :class="{ active: index === breadcrumb.length - 1 }"
      >
        <router-link v-if="item.to && index !== breadcrumb.length - 1" :to="item.to">
          {{ item.label }}
        </router-link>
        <span v-else>{{ item.label }}</span>
      </li>
    </ol>
  </nav>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { computed } from 'vue'

const route = useRoute()

const breadcrumb = computed(() => {
  return route.meta.breadcrumb || [{ label: 'Inicio', to: '/' }]
})
</script>

<style scoped>
.breadcrumb ol {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  gap: 0.5em;
}

.breadcrumb li::after {
  content: '/';
  margin-left: 0.5em;
}

.breadcrumb li:last-child::after {
  content: '';
}

.breadcrumb li.active span {
  font-weight: bold;
  color: #555;
}

.breadcrumb li a {
  text-decoration: none;
  color: #007bff;
}

.breadcrumb li a:hover {
  text-decoration: underline;
}
</style>
