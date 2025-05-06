<script setup lang="ts">
import { RouterView } from 'vue-router'
import Footer from './components/Footer.vue';
import Navbar from './components/Navbar.vue';
import NavbarNoLoged from './components/NavbarNoLoged.vue'

import { inject, watch } from 'vue';
import { useRouter } from 'vue-router';

const auth = inject<{ isLoggedIn: boolean }>('auth')!;
const setAuth = inject<Function>('setAuth')!;
const router = useRouter();

function logout() {
  localStorage.removeItem('token');
  setAuth(false);
  router.push('/');
}



</script>

<template>
  <nav v-if="auth.isLoggedIn">
    <Navbar></Navbar>
  </nav>
  <nav v-else>
    <NavbarNoLoged></NavbarNoLoged>
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
