<script setup lang="ts">
import { RouterView } from 'vue-router'
import Footer from './components/Footer.vue';
import Navbar from './components/Navbar.vue';

</script>

<template>
  <nav>
    <Navbar></Navbar>
  </nav>
  <main class="container mt-4">
    <RouterView />
  </main>
  <footer>
    <Footer></Footer>
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
</style>
