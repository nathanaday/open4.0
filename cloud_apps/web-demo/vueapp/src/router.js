// router.js
import { createRouter, createWebHistory } from 'vue-router';
import Dash1 from './components/dash1.vue';
import WelcomeComponent from './components/welcomecomponent.vue';
import PointView from './components/subcomponents/pointview.vue';

const routes = [
  {
    path: '/',
    name: 'Welcome',
    component: WelcomeComponent,
  },
  {
    path: '/demo',
    name: 'Demo',
    component: Dash1,
  },
  {
    path: '/pointview',
    name: 'PointView',
    component: PointView,
  }
];

const router = createRouter({
  history: createWebHistory(''),
  routes,
});

export default router;
