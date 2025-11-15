import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import BooksList from '../views/BooksList.vue'
import BookDetails from '../views/BookDetails.vue'
import ReadersList from '../views/ReadersList.vue'
import LoanBook from '../views/LoanBook.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/books', component: BooksList },
  { path: '/books/:id', component: BookDetails },
  { path: '/readers', component: ReadersList },
  { path: '/loan', component: LoanBook },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
