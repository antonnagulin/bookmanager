<template>
  <div class="page">

    <h1 class="title">Каталог книг</h1>

    <div class="books-grid">
      <div
        v-for="book in books"
        :key="book.id"
        class="book-card"
      >
        <img
          v-if="book.cover"
          :src="book.cover"
          class="bigcover"
        />
        <div v-else class="no-cover">Нет обложки</div>

        <h3 class="book-title-name">{{ book.title }}</h3>
        <p class="book-author-name">{{ book.author }}</p>

        <p class="copies">
          Доступно: <b>{{ book.available_copies }}</b> из {{ book.total_copies }}
        </p>


        <router-link :to="`/books/${book.id}`">
            <button class="details-btn">
                Подробнее
            </button>
        </router-link>

      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import '../assets/css/books_list_for_reader.css'

const books = ref([])

const loadBooks = async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/book/')
    books.value = res.data
  } catch (e) {
    console.error("Ошибка загрузки книг:", e)
  }
}

onMounted(loadBooks)
</script>
