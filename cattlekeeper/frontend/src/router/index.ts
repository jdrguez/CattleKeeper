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
    { path: '/', name: 'home', component: HomeView, meta: { breadcrumb: [{ label: 'Home', to: '/dashboard' }] , hideSidebar: true } },
    { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound, meta: { breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Not found' }] } },

    // Accounts
    { path: '/login', name: 'Login', component: LoginView, meta: { breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Login' }], hideSidebar: true } },
    { path: '/signup', name: 'signup', component: SignupView, meta: { breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Sign up' }], hideSidebar: true } },
    { path: '/logout', name: 'logout', component: LogoutView, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Logout' }], hideSidebar: true } },
    { path: '/account', name: 'account', component: UserProfile, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Profile' }] } },
    { path: '/account/edit', component: EditUserProfile, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, {label: 'Profile', to: '/account'},{ label: 'Edit profile' }] } },

    // General
    { path: '/about', name: 'about', component: AboutView, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'About' }] } },
    { path: '/dashboard', name: 'dashboard', component: DashboardView, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Dashboard' }], hideSidebar: true } },
   
    // Batches
    { path: '/batches', name: 'batch-list', component: BatchList, meta: { requiresAuth: true ,breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Batches' }] } },
    { path: '/batch/:batch_slug', name: 'BatchDetail', component: BatchDetail, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Batches' , to: '/batches'}, {label: 'Batch details'}] } },
    { path: '/batch/create', name: 'BatchCreate', component: BatchCreate, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Batches' , to: '/batches'},{ label: 'Create batch' }] } },
    { path: '/batch/:batch_slug/update', name: 'BatchUpdate', component: BatchUpdate, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Batches' , to: '/batches'}, { label: 'Update batch' }] } },
    { path: '/batch/:batch_slug/delete', name: 'batch-delete', component: BatchDelete, props: true, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Batches' , to: '/batches'}, { label: 'Delete batch' }] } },
    { path: '/batches/:batch_slug/animals', name: 'BatchAnimalList', component: BatchAnimalList, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Batches' , to: '/batches'},{ label: 'Batch animals' }] } },

    // Animals
    { path: '/batches/:batch_slug/animals/:animal_slug', name: 'AnimalDetail', component: AnimalDetail, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Animal details' }] } },
    { path: '/batches/:batch_slug/animals/create', name: 'AnimalCreate', component: AnimalCreate, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Create animal' }] } },
    { path: '/batch/:batch_slug/animals/:animal_slug/update', name: 'AnimalUpdate', component: AnimalUpdate, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, {label: 'Animals', to:'/batches'},{ label: 'Update animal' }] } },
    { path: '/farm/batch/:batch_slug/animals/:animal_slug/delete', name: 'AnimalDelete', component: AnimalDelete, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Delete animal' }] } },

    // Health
    { path: '/batches/:batch_slug/animals/:animal_slug/health/create', name: 'HealthEventCreate', component: HealthEventCreate, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Create health event' }] } },

    // Production
    { path: '/batch/:batch_slug/productions', name: 'ProductionList', component: ProductionList, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Production' }] } },
    { path: '/batch/:batch_slug/production/create', name: 'ProductionCreate', component: ProductionCreate, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Create production' }] } },
    { path: '/batch/:batch_slug/production/:production_pk/edit', name: 'ProductionEdit', component: ProductionEdit, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Edit production' }] } },

    // Finances
    { path: '/finances/expenses', name: 'expenses', component: Expenses, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Expenses' }] } },
    { path: '/finances/expenses/create', name: 'expense-create', component: ExpenseCreate, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, {label: 'Expenses', to:'/finances/expenses'},{ label: 'Create expense' }] } },
    { path: '/finances/incomes', name: 'incomes', component: Incomes, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Incomes' }] } },
    { path: '/finances/incomes/create', name: 'create-income', component: CreateIncome, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, {label: 'Incomes', to:'/finances/incomes'},{ label: 'Create income' }] } },
    { path: '/finances/report/', name: 'report', component: Report, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard'}]}},

    // Map
    { path: '/map', name: 'FarmMap', component: FarmMap, meta: { breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Map' }], requiresAuth: true } },

    // Subscription
    { path: '/plans', name: 'PlansView', component: PlansView, meta: { requiresAuth: true, breadcrumb: [ { label: 'Home', to: '/dashboard' },{ label: 'Available plans' }]}},
    { path: '/plans/subscribe/:planId', name: 'SubscribeToPlan', component: SubscribeToPlan, props: true, meta: { requiresAuth: true, breadcrumb: [{ label: 'Home', to: '/dashboard' }, { label: 'Available plans', to: '/plans' }, { label: 'Subscribe' }]}},

  ],
})


router.beforeEach(async (to, from, next) => {
  const subscription = useSubscriptionStore()

  const loggedIn = !!localStorage.getItem('token')
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth)
  if (requiresAuth && !loggedIn) {
    return next('/')
  }

  if (!subscription.loading && subscription.isActive === false && to.meta.requiresSubscription) {
    return next('/plans')
  }

  if (to.meta.requiresSubscription && !subscription.loading && subscription.isActive === null) {
    await subscription.checkSubscription()
    if (!subscription.isActive) {
      return next('/plans')
    }
  }

  next()
})


export default router
