<template>
  <div class="px-3 py-2 border-bottom" id="container-nav">
    <div class="container">
      <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
          
          <RouterLink
            :to="isLoggedIn ? '/dashboard' : '/'"
            class="d-flex align-items-center my-2 my-lg-0 me-lg-auto text-white text-decoration-none">
            <img class="logo" src="../assets/img/logo.webp" alt="Logo" />
          </RouterLink>
        
        <ul class="nav col-12 col-lg-auto my-2 justify-content-center my-md-0 text-small">

          <li v-if="!isLoggedIn">
            <NavButton 
              to_router=""
              class_str="nav-link text-secondary"
              svg_class="bi bi-house d-block mx-auto mb-1"
              :name="t('home')"
            />
          </li>

          <li v-if="!isLoggedIn">
            <NavButton 
              to_router="login"
              class_str="nav-link text-white"
              svg_class="bi bi-door-open d-block mx-auto mb-1"
              :name="t('login')"
            />
          </li>

          <li v-if="isLoggedIn">
            <NavButton 
              to_router="dashboard"
              class_str="nav-link text-white"
              svg_class="bi bi-speedometer d-block mx-auto mb-1"
              :name="t('dashboard')"
            />
          </li>

          <li v-if="isLoggedIn">
            <NavButton 
              to_router="products"
              class_str="nav-link text-white"
              svg_class="bi bi-bag d-block mx-auto mb-1"
              :name="t('products')"
            />
          </li>

          <li v-if="isLoggedIn" class="nav-item dropdown">
            <a class="nav-link dropdown-toggle text-white" href="#" role="button" data-bs-toggle="dropdown">
              <i class="bi bi-flower3 d-block mx-auto mb-1"></i>
              {{ t('farm') }}
            </a>
            <ul class="dropdown-menu">
              <li>
                <RouterLink to="/batches" class="dropdown-item">{{ t('batch-list') }}</RouterLink>
              </li>
              <li>
                <RouterLink to="/finances/expenses" class="dropdown-item">{{ t('finances') }}</RouterLink>
              </li>
            </ul>
          </li>

          <li v-if="isLoggedIn">
            <NavButton 
              to_router="account"
              class_str="nav-link text-white"
              svg_class="bi bi-person d-block mx-auto mb-1"
              :name="t('account')"
            />
          </li>
          
          <li v-if="isLoggedIn">
            <NavButton 
              to_router="logout"
              class_str="nav-link text-white"
              svg_class="bi bi-door-closed d-block mx-auto mb-1"
              :name="t('logout')"
            />
          </li>

          <li>
            <button @click="changeLanguage" style="background: none; border: none;">{{ t('change') }}</button>
          </li>

        </ul>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useI18n } from 'vue-i18n';
import { inject, reactive, computed } from 'vue';
import NavButton from './NavButton.vue';

const auth = inject<{ isLoggedIn: boolean }>('auth')!;
const reactiveAuth = reactive(auth);
const { t, locale } = useI18n();

const isLoggedIn = computed(() => reactiveAuth.isLoggedIn);

const changeLanguage = () => {
  locale.value = locale.value === 'en' ? 'es' : 'en';
};
</script>

<style>
#container-nav {
  background-color: #015730;
  color: black !important;
}

.nav-link {
  color: white !important;
}

.nav-link:hover {
  text-decoration: underline;
  text-decoration-color: #FF8800;
}

.logo {
  height: 60px;
  margin-bottom: 10px;
}
</style>
