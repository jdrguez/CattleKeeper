import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import DashboardView from '../views/DashboardView.vue'
import ProductsView from '@/views/ProductsView.vue'
import AccountView from '@/views/AccountView.vue'
import OrderDetail from '@/views/OrderDetail.vue'
import WishlistView from '@/views/WishlistView.vue'
import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'





const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/login',
      name: 'Login',
      component: LoginView,
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView,
    },
    {
      path: '/logout',
      name: 'logout',
      component: LogoutView,
      meta: { requiresAuth: true }
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView,
      meta: { requiresAuth: true }
    },
    {
      path: '/account',
      name: 'account',
      component: AccountView,
      meta: { requiresAuth: true }
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView,
      meta: { requiresAuth: true }
    },
    {
      path: '/products',
      name: 'products',
      component: ProductsView,
      meta: { requiresAuth: true }
    },
    {
      path: '/order/:id',
      name: 'order',
      component: OrderDetail,
      meta: { requiresAuth: true }
    },
    {
      path: '/wishlist',
      name: 'Wishlist',
      component: WishlistView,
      meta: { requiresAuth: true }
      },
  ],
})


router.beforeEach((to, from, next) => {
  const loggedIn = !!localStorage.getItem('token')
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  if (requiresAuth && !loggedIn) {
    next(('/'))
  } else {
    next()
  }
})




export default router
