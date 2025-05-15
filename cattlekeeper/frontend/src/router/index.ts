import { createRouter, createWebHistory } from 'vue-router'

// Vistas generales
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import DashboardView from '../views/DashboardView.vue'
import NotFound from '@/views/NotFound.vue'
import OrderDetail from '@/views/OrderDetail.vue'
import WishlistView from '@/views/WishlistView.vue'
import ProductsView from '@/views/ProductsView.vue'

// Cuentas
import LoginView from '@/views/accounts/LoginView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'
import SignupView from '@/views/accounts/SignupView.vue'
import AccountView from '@/views/accounts/AccountView.vue'
import UserProfile from '@/views/accounts/UserProfile.vue'
import EditUserProfile from '@/views/accounts/EditUserProfile.vue'

// Batches
import BatchList from '@/views/farm/batches/BatchList.vue'
import BatchDetail from '@/views/farm/batches/BatchDetail.vue'
import BatchCreate from '@/views/farm/batches/BatchCreate.vue'
import BatchUpdate from '@/views/farm/batches/BatchUpdate.vue'
import BatchDelete from '@/views/farm/batches/BatchDelete.vue'
import BatchAnimalList from '@/views/farm/batches/BatchAnimalList.vue'

// Animales
import AnimalDetail from '@/views/farm/animals/AnimalDetail.vue'
import AnimalCreate from '@/views/farm/animals/AnimalCreate.vue'
import AnimalUpdate from '@/views/farm/animals/AnimalUpdate.vue'
import AnimalDelete from '@/views/farm/animals/AnimalDelete.vue'

// Salud
import HealthEventCreate from '@/views/farm/health/HealthEventCreate.vue'

// Producción
import ProductionList from '@/views/farm/production/ProductionList.vue'
import ProductionCreate from '@/views/farm/production/ProductionCreate.vue'
import ProductionEdit from '@/views/farm/production/ProductionEdit.vue'

// Finanzas
import Expenses from '@/views/farm/finances/Expenses.vue'
import ExpenseCreate from '@/views/farm/finances/ExpenseCreate.vue'
import ExpenseUpdate from '@/views/farm/finances/ExpenseUpdate.vue'
import Incomes from '@/views/farm/finances/Incomes.vue'
import CreateIncome from '@/views/farm/finances/CreateIncome.vue'
import EditIncome from '@/views/farm/finances/EditIncome.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: HomeView },
    { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound },

    // Cuentas
    { path: '/login', name: 'Login', component: LoginView },
    { path: '/signup', name: 'signup', component: SignupView },
    { path: '/logout', name: 'logout', component: LogoutView, meta: { requiresAuth: true } },
    { path: '/account', name: 'account', component: AccountView, meta: { requiresAuth: true } },
    { path: '/perfil', component: UserProfile},
    { path: '/perfil/editar',component: EditUserProfile},

    // Generales
    { path: '/about', name: 'about', component: AboutView, meta: { requiresAuth: true } },
    { path: '/dashboard', name: 'dashboard', component: DashboardView, meta: { requiresAuth: true } },
    { path: '/products', name: 'products', component: ProductsView, meta: { requiresAuth: true } },
    { path: '/order/:id', name: 'order', component: OrderDetail, meta: { requiresAuth: true } },
    { path: '/wishlist', name: 'Wishlist', component: WishlistView, meta: { requiresAuth: true } },

    // Batches
    { path: '/batches', name: 'batch-list', component: BatchList },
    { path: '/batch/:batch_slug', name: 'BatchDetail', component: BatchDetail },
    { path: '/batch/create', name: 'BatchCreate', component: BatchCreate },
    { path: '/batch/:batch_slug/update', name: 'BatchUpdate', component: BatchUpdate },
    { path: '/batch/:batch_slug/delete', name: 'batch-delete', component: BatchDelete, props: true },
    { path: '/batches/:batch_slug/animals', name: 'BatchAnimalList', component: BatchAnimalList },

    // Animales
    { path: '/batches/:batch_slug/animals/:animal_slug', name: 'AnimalDetail', component: AnimalDetail },
    { path: '/batches/:batch_slug/animals/create', name: 'AnimalCreate', component: AnimalCreate },
    { path: '/batch/:batch_slug/animals/:animal_slug/update', name: 'AnimalUpdate', component: AnimalUpdate },
    { path: '/farm/batch/:batch_slug/animals/:animal_slug/delete', name: 'AnimalDelete', component: AnimalDelete },

    // Salud
    { path: '/batches/:batch_slug/animals/:animal_slug/health/create', name: 'HealthEventCreate', component: HealthEventCreate },

    // Producción
    { path: '/batch/:batch_slug/productions', name: 'ProductionList', component: ProductionList },
    { path: '/batch/:batch_slug/production/create', name: 'ProductionCreate', component: ProductionCreate },
    { path: '/batch/:batch_slug/production/:production_pk/edit', name: 'ProductionEdit', component: ProductionEdit },

    // Finanzas
    { path: '/finances/expenses', name: 'expenses', component: Expenses },
    { path: '/finances/expenses/create', name: 'expense-create', component: ExpenseCreate },
    { path: '/finances/expenses/:expense_pk/update', name: 'expense-update', component: ExpenseUpdate },
    { path: '/finances/incomes', name: 'incomes', component: Incomes },
    { path: '/finances/incomes/create', name: 'create-income', component: CreateIncome },
    { path: '/finances/incomes/:id/edit', name: 'edit-income', component: EditIncome },
  ],
})

router.beforeEach((to, from, next) => {
  const loggedIn = !!localStorage.getItem('token')
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth)
  if (requiresAuth && !loggedIn) {
    next('/')
  } else {
    next()
  }
})

export default router
