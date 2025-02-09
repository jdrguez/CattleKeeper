import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import DashboardView from '../views/DashboardView.vue'
import ProductsView from '@/views/ProductsView.vue'
import AccountView from '@/views/AccountView.vue'
import OrderDetail from '@/views/OrderDetail.vue'
import WishlistView from '@/views/WishlistView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView,
    },
    {
      path: '/account',
      name: 'account',
      component: AccountView,
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView,
    },
    {
      path: '/products',
      name: 'products',
      component: ProductsView,
    },
    {
      path: '/order/:id',
      name: 'order',
      component: OrderDetail,
    },
    {
      path: '/wishlist',
      name: 'Wishlist',
      component: WishlistView,
      },
  ],
})

export default router
