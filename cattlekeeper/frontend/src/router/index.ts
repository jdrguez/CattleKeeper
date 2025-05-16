import { createRouter, createWebHistory } from 'vue-router'

// Vistas generales
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import DashboardView from '../views/DashboardView.vue'
import NotFound from '@/views/NotFound.vue'
import OrderDetail from '@/views/orders/OrderDetail.vue'
import WishlistView from '@/views/WishlistView.vue'
import ProductsView from '@/views/ProductsView.vue'
import FarmMap from '@/views/farm/map/FarmMap.vue'

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
    { path: '/', name: 'home', component: HomeView, meta: { breadcrumb: 'Inicio' } },
    { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound, meta: { breadcrumb: 'No encontrado' } },

    // Cuentas
    { path: '/login', name: 'Login', component: LoginView, meta: { breadcrumb: 'Iniciar sesión' } },
    { path: '/signup', name: 'signup', component: SignupView, meta: { breadcrumb: 'Registro' } },
    { path: '/logout', name: 'logout', component: LogoutView, meta: { requiresAuth: true, breadcrumb: 'Cerrar sesión' } },
    { path: '/account', name: 'account', component: UserProfile, meta: { requiresAuth: true, breadcrumb: 'Perfil' } },
    { path: '/account/edit', component: EditUserProfile, meta: { requiresAuth: true, breadcrumb: 'Editar perfil' } },

    // Generales
    { path: '/about', name: 'about', component: AboutView, meta: { requiresAuth: true, breadcrumb: 'Acerca de' } },
    { path: '/dashboard', name: 'dashboard', component: DashboardView, meta: { requiresAuth: true, breadcrumb: 'Panel' } },
    { path: '/products', name: 'products', component: ProductsView, meta: { requiresAuth: true, breadcrumb: 'Productos' } },
    { path: '/order/:id', name: 'order', component: OrderDetail, meta: { requiresAuth: true, breadcrumb: 'Detalle orden' } },
    { path: '/wishlist', name: 'Wishlist', component: WishlistView, meta: { requiresAuth: true, breadcrumb: 'Lista deseos' } },

    // Batches
    { path: '/batches', name: 'batch-list', component: BatchList, meta: { breadcrumb: 'Lotes' } },
    { path: '/batch/:batch_slug', name: 'BatchDetail', component: BatchDetail, meta: { breadcrumb: 'Detalle lote' } },
    { path: '/batch/create', name: 'BatchCreate', component: BatchCreate, meta: { breadcrumb: 'Crear lote' } },
    { path: '/batch/:batch_slug/update', name: 'BatchUpdate', component: BatchUpdate, meta: { breadcrumb: 'Actualizar lote' } },
    { path: '/batch/:batch_slug/delete', name: 'batch-delete', component: BatchDelete, props: true, meta: { breadcrumb: 'Eliminar lote' } },
    { path: '/batches/:batch_slug/animals', name: 'BatchAnimalList', component: BatchAnimalList, meta: { breadcrumb: 'Animales lote' } },

    // Animales
    { path: '/batches/:batch_slug/animals/:animal_slug', name: 'AnimalDetail', component: AnimalDetail, meta: { breadcrumb: 'Detalle animal' } },
    { path: '/batches/:batch_slug/animals/create', name: 'AnimalCreate', component: AnimalCreate, meta: { breadcrumb: 'Crear animal' } },
    { path: '/batch/:batch_slug/animals/:animal_slug/update', name: 'AnimalUpdate', component: AnimalUpdate, meta: { breadcrumb: 'Actualizar animal' } },
    { path: '/farm/batch/:batch_slug/animals/:animal_slug/delete', name: 'AnimalDelete', component: AnimalDelete, meta: { breadcrumb: 'Eliminar animal' } },

    // Salud
    { path: '/batches/:batch_slug/animals/:animal_slug/health/create', name: 'HealthEventCreate', component: HealthEventCreate, meta: { breadcrumb: 'Crear evento salud' } },

    // Producción
    { path: '/batch/:batch_slug/productions', name: 'ProductionList', component: ProductionList, meta: { breadcrumb: 'Producción' } },
    { path: '/batch/:batch_slug/production/create', name: 'ProductionCreate', component: ProductionCreate, meta: { breadcrumb: 'Crear producción' } },
    { path: '/batch/:batch_slug/production/:production_pk/edit', name: 'ProductionEdit', component: ProductionEdit, meta: { breadcrumb: 'Editar producción' } },

    // Finanzas
    { path: '/finances/expenses', name: 'expenses', component: Expenses, meta: { breadcrumb: 'Gastos' } },
    { path: '/finances/expenses/create', name: 'expense-create', component: ExpenseCreate, meta: { breadcrumb: 'Crear gasto' } },
    { path: '/finances/expenses/:expense_pk/update', name: 'expense-update', component: ExpenseUpdate, meta: { breadcrumb: 'Actualizar gasto' } },
    { path: '/finances/incomes', name: 'incomes', component: Incomes, meta: { breadcrumb: 'Ingresos' } },
    { path: '/finances/incomes/create', name: 'create-income', component: CreateIncome, meta: { breadcrumb: 'Crear ingreso' } },
    { path: '/finances/incomes/:id/edit', name: 'edit-income', component: EditIncome, meta: { breadcrumb: 'Editar ingreso' } },

    //Mapa
    { path: '/map', name:'FarmMap', component: FarmMap, meta: {breadcrumb: 'Mapa', requiresAuth: true}},

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
