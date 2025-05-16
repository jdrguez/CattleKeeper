import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import 'bootstrap-icons/font/bootstrap-icons.css';
import i18n from './i18n/index';
import './assets/main.css';

import { createApp, reactive } from 'vue';
import { createPinia } from 'pinia';
import Toast, {POSITION} from 'vue-toastification'
import 'vue-toastification/dist/index.css'
import App from './App.vue';
import router from './router';

const app = createApp(App);
const authState = reactive({
    isLoggedIn: !!localStorage.getItem('token'),
  });
app.use(createPinia());
app.use(router);
app.use(i18n);
app.use(Toast,{
  position: POSITION.BOTTOM_RIGHT,
  timeout: 3000,
})

app.provide('auth', authState);
app.provide('setAuth', (value: boolean) => { authState.isLoggedIn = value; });
app.mount('#app');