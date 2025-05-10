<script setup>
import { RouterLink } from 'vue-router'
import { computed } from 'vue'
const props = defineProps({
  to_router: String,
  class_str: String,
  svg_class: String,
  xlink: String,
  name: String,
})


const fullPath = computed(() => {
  if (!props.to_router) return '/'
  return props.to_router.startsWith('/') ? props.to_router : '/' + props.to_router
})




</script>

<template>
  <RouterLink :to="fullPath" :class="props.class_str">
    <i :class="props.svg_class" width="24" height="24">
    </i>
    {{ props.name }}
  </RouterLink>
</template>
