import { createRouter, createWebHistory } from 'vue-router'

// Vistas generales
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import DashboardView from '../views/DashboardView.vue'
import NotFound from '@/views/NotFound.vue'
import FarmMap from '@/views/farm/map/FarmMap.vue'

// Cuentas
import LoginView from '@/views/accounts/LoginView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'
import SignupView from '@/views/accounts/SignupView.vue'
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
import Incomes from '@/views/farm/finances/Incomes.vue'
import CreateIncome from '@/views/farm/finances/CreateIncome.vue'
import Report from '@/views/farm/finances/Report.vue'

// Subscripciones
import SubscribeToPlan from '@/views/accounts/SubscribeToPlan.vue'
import PlansView from '@/views/accounts/PlansView.vue'

//Store
import { useSubscriptionStore } from '@/stores/subscription'




const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: HomeView, meta: { breadcrumb: [{ label: 'Inicio', to: '/dashboard' }] , hideSidebar: true } },
    { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound, meta: { breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'No encontrado' }] } },

    // Cuentas
    { path: '/login', name: 'Login', component: LoginView, meta: { breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Iniciar sesión' }], hideSidebar: true } },
    { path: '/signup', name: 'signup', component: SignupView, meta: { breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Registro' }], hideSidebar: true } },
    { path: '/logout', name: 'logout', component: LogoutView, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Cerrar sesión' }], hideSidebar: true } },
    { path: '/account', name: 'account', component: UserProfile, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Perfil' }] } },
    { path: '/account/edit', component: EditUserProfile, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, {label: 'Perfil', to: '/account'},{ label: 'Editar perfil' }] } },

    // Generales
    { path: '/about', name: 'about', component: AboutView, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Acerca de' }] } },
    { path: '/dashboard', name: 'dashboard', component: DashboardView, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Panel' }], hideSidebar: true } },
   
    // Batches
    { path: '/batches', name: 'batch-list', component: BatchList, meta: { requiresAuth: true ,breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Lotes' }] } },
    { path: '/batch/:batch_slug', name: 'BatchDetail', component: BatchDetail, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Lotes' , to: '/batches'}, {label: 'Detalle del lote'}] } },
    { path: '/batch/create', name: 'BatchCreate', component: BatchCreate, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Lotes' , to: '/batches'},{ label: 'Crear lote' }] } },
    { path: '/batch/:batch_slug/update', name: 'BatchUpdate', component: BatchUpdate, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Lotes' , to: '/batches'}, { label: 'Actualizar lote' }] } },
    { path: '/batch/:batch_slug/delete', name: 'batch-delete', component: BatchDelete, props: true, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Lotes' , to: '/batches'}, { label: 'Eliminar lote' }] } },
    { path: '/batches/:batch_slug/animals', name: 'BatchAnimalList', component: BatchAnimalList, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Lotes' , to: '/batches'},{ label: 'Animales lote' }] } },

    // Animales
    { path: '/batches/:batch_slug/animals/:animal_slug', name: 'AnimalDetail', component: AnimalDetail, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Detalle animal' }] } },
    { path: '/batches/:batch_slug/animals/create', name: 'AnimalCreate', component: AnimalCreate, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Crear animal' }] } },
    { path: '/batch/:batch_slug/animals/:animal_slug/update', name: 'AnimalUpdate', component: AnimalUpdate, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, {label: 'Animales', to:'/batches'},{ label: 'Actualizar animal' }] } },
    { path: '/farm/batch/:batch_slug/animals/:animal_slug/delete', name: 'AnimalDelete', component: AnimalDelete, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Eliminar animal' }] } },

    // Salud
    { path: '/batches/:batch_slug/animals/:animal_slug/health/create', name: 'HealthEventCreate', component: HealthEventCreate, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Crear evento salud' }] } },

    // Producción
    { path: '/batch/:batch_slug/productions', name: 'ProductionList', component: ProductionList, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Producción' }] } },
    { path: '/batch/:batch_slug/production/create', name: 'ProductionCreate', component: ProductionCreate, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Crear producción' }] } },
    { path: '/batch/:batch_slug/production/:production_pk/edit', name: 'ProductionEdit', component: ProductionEdit, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Editar producción' }] } },

    // Finanzas
    { path: '/finances/expenses', name: 'expenses', component: Expenses, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Gastos' }] } },
    { path: '/finances/expenses/create', name: 'expense-create', component: ExpenseCreate, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, {label: 'Gastos', to:'/finances/expenses'},{ label: 'Crear gasto' }] } },
    { path: '/finances/incomes', name: 'incomes', component: Incomes, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Ingresos' }] } },
    { path: '/finances/incomes/create', name: 'create-income', component: CreateIncome, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, {label: 'Ingresos', to:'/finances/incomes'},{ label: 'Crear ingreso' }] } },
    { path: '/finances/report/', name: 'report', component: Report, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard'}]}},

    // Mapa
    { path: '/map', name: 'FarmMap', component: FarmMap, meta: { breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Mapa' }], requiresAuth: true } },

    //Subscripcion
    { path: '/plans', name: 'PlansView', component: PlansView, meta: { requiresAuth: true, breadcrumb: [ { label: 'Inicio', to: '/dashboard' },{ label: 'Planes disponibles' }]}},
    { path: '/plans/subscribe/:planId', name: 'SubscribeToPlan', component: SubscribeToPlan, props: true, meta: { requiresAuth: true, breadcrumb: [{ label: 'Inicio', to: '/dashboard' }, { label: 'Planes disponibles', to: '/plans' }, { label: 'Subscribirse' }]}},

  ],
})



router.beforeEach(async (to, from, next) => {
  const subscription = useSubscriptionStore()

  // Mantengo intacta tu parte de login
  const loggedIn = !!localStorage.getItem('token')
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth)
  if (requiresAuth && !loggedIn) {
    return next('/')
  }

  // Si la suscripción está cargada y no es activa y la ruta requiere suscripción, redirige a /plans
  if (!subscription.loading && subscription.isActive === false && to.meta.requiresSubscription) {
    return next('/plans')
  }

  // Si la ruta requiere suscripción, y no sabemos si está activa (isActive === null), la comprobamos
  if (to.meta.requiresSubscription && !subscription.loading && subscription.isActive === null) {
    await subscription.checkSubscription()
    if (!subscription.isActive) {
      return next('/plans')
    }
  }

  next()
})




export default router
