<template>
  <nav aria-label="breadcrumb">
    <ol class="breadcrumb">
      <li
        v-for="(crumb, index) in breadcrumbs"
        :key="index"
        class="breadcrumb-item"
        :class="{ active: index === breadcrumbs.length - 1 }"
        :aria-current="index === breadcrumbs.length - 1 ? 'page' : null"
      >
        <template v-if="index !== breadcrumbs.length - 1">
          <RouterLink v-if="crumb.to" :to="crumb.to">{{ crumb.label }}</RouterLink>
          <span v-else>{{ crumb.label }}</span>
        </template>
        <span v-else>{{ crumb.label }}</span>
      </li>
    </ol>
  </nav>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  breadcrumbs: {
    type: Array,
    required: true,
    validator: (val) =>
      val.every(
        (item) =>
          typeof item.label === 'string' &&
          ('to' in item ? typeof item.to === 'string' : true)
      ),
  },
})
</script>

<style scoped>
.breadcrumb {
  display: flex;
  gap: 0.5rem;
  list-style: none;
  padding: 0;
  margin: 0;
}
.breadcrumb-item::after {
  content: "/";
  margin-left: 0.5rem;
}
.breadcrumb-item:last-child::after {
  content: "";
}
.breadcrumb-item.active {
  font-weight: bold;
}
</style>
