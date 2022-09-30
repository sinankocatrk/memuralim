import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import saglik1 from '../views/saglik1.vue'
import saglik2 from '../views/saglik2.vue'
import saglik3 from '../views/saglik3.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/saglik1',
      name: 'saglik1',
      component: saglik1
    },
    {
      path: '/saglik2',
      name: 'saglik2',
      component: saglik2
    },
    {
      path: '/saglik3',
      name: 'saglik3',
      component: saglik3
    },
  ]
})

export default router
