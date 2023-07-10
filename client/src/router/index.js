import { createRouter, createWebHistory } from 'vue-router'
import BooksPath from '../components/BooksPath.vue'




 const  routes =[
  {
    path: '/',
    name: 'BooksPath',
    component: BooksPath,
  },
  
  ];
  
const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router
