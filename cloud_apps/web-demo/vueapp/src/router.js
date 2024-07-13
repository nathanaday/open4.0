// router.js
import { createRouter, createWebHistory } from 'vue-router';
import PointCloudDemo from './components/pointclouddemo.vue';

const routes = [
  {
    path: '/',
    name: 'PointCloud',
    component: PointCloudDemo,
  },
];

const router = createRouter({
  history: createWebHistory(''),
  routes,
});

export default router;
