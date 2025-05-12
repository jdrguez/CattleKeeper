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
import BatchList from '@/views/BatchList.vue'
import BatchDetail from '@/views/BatchDetail.vue'
import BatchCreate from '@/views/BatchCreate.vue'
import BatchUpdate from '@/views/BatchUpdate.vue'
import AnimalDelete from '@/views/AnimalDelete.vue'
import BatchDelete from '@/views/BatchDelete.vue'
import NotFound from '@/views/NotFound.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound },
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
      {
        path: '/batches',
        name: 'batch-list',
        component: BatchList,
      },
      {
        path: '/batch/:batch_slug',
        name: 'BatchDetail',
        component: BatchDetail
      },
      {
        path: '/batch/create',
        name: 'BatchCreate',
        component: BatchCreate
      },
      {
        path: '/batch/:batch_slug/update',
        name: 'BatchUpdate',
        component: BatchUpdate
      }, 
      {
        path: '/batches/:batch_slug/animals',
        name: 'BatchAnimalList',
        component: () => import('@/views/BatchAnimalList.vue')
      },
      {
        path: '/batches/:batch_slug/animals/:animal_slug',
        name: 'AnimalDetail',
        component: () => import('@/views/AnimalDetail.vue')
      },      
      {
        path: '/batches/:batch_slug/animals/create',
        name: 'AnimalCreate',
        component: () => import('@/views/AnimalCreate.vue')
      },
      {
        path: '/batch/:batch_slug/animals/:animal_slug/update',
        name: 'AnimalUpdate',
        component: () => import('@/views/AnimalUpdate.vue')
      },
      {
        path: '/farm/batch/:batch_slug/animals/:animal_slug/delete',
        name: 'AnimalDelete',
        component: AnimalDelete
      },
      {
        path: '/batch/:batch_slug/delete',  
        name: 'batch-delete',  
        component: BatchDelete,  
        props: true 
      },
      {
      path: '/batches/:batch_slug/animals/:animal_slug/health/create',
      name: 'HealthEventCreate',
      component: () => import('@/views/HealthEventCreate.vue')
    }

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
