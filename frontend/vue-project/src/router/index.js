import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import BooksList from '../components/BooksList.vue'
import BookDetails from '../views/BookDetails.vue'
import ReadersList from '../views/ReadersList.vue'
import LoanBook from '../views/LoanBook.vue'
import LocationsList from '../components/LocationsList.vue'
import BooksCreate from '../components/BooksCreate.vue'


const routes = [
    { path: '/', component: Home },
    { path: '/books_list', component: BooksList },
    { path: '/books_create', component: BooksCreate },
    { path: '/books/:id', component: BookDetails },
    { path: '/readers', component: ReadersList },
    { path: '/loan', component: LoanBook },
    { path: '/locations', component: LocationsList }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router