<script setup lang="ts">
import { RouterView, useRoute } from 'vue-router' 
import Footer from './components/Footer.vue';
import Navbar from './components/Navbar.vue';
import Breadcrumbs from './components/utils/Breadcrumbs.vue';

const route = useRoute()




</script>

<template>
  <nav>
    <Navbar></Navbar>
  </nav>
  <main class="container mt-4">
    <Breadcrumbs :items="route.meta.breadcrumb || []" />
    <RouterView />
  </main>
  <footer>
    <Footer />
  </footer>
</template>

<style>
header {
  width: 100%;
}

main {
  padding: 20px;
  width: 100%;
}

body.theme-dark {
  background-color: #121212 !important;
  color: #e0e0e0;
}

body.theme-light {
  background-color: #ffffff !important;
  color: #000000;
}

body.theme-dark a {
  color: #90caf9;
}

body.theme-dark .card {
  background-color: #1e1e1e;
  border-color: #333;
}



</style>
