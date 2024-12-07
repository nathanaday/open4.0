// router.js
import { createRouter, createWebHistory } from 'vue-router';
import WelcomeComponent from './components/welcomecomponent.vue';

const routes = [
  {
    path: '/',
    name: 'WelcomeComponent',
    component: WelcomeComponent,
  },
];

const router = createRouter({
  history: createWebHistory(''),
  routes,
});

export default router;
