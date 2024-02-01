import { createApp } from 'vue';
import { BootstrapIconsPlugin } from 'bootstrap-icons-vue';
import App from './App.vue';
import router from './router';
import store from './store/index';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import VueSelect from 'vue-select';


const app = createApp(App);

app.use(BootstrapIconsPlugin);
app.use(router);
app.use(store);
app.component('v-select', VueSelect); // Register the component

app.mount('#app');

export const eventBus = app;