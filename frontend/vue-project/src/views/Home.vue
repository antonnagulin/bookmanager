<!-- src/views/Home.vue -->
<template>
  <div class="home">
    <h1>Добро пожаловать в библиотеку</h1>
    <p>Найдите свою следующую любимую книгу</p>
    <router-link to="/books" class="btn">Перейти к каталогу</router-link>

    <section v-if="featuredBooks.length > 0" class="featured">
      <h2>Рекомендуем</h2>
      <div class="books-grid">
        <div v-for="book in featuredBooks" :key="book.id" class="book-card">
          <img :src="book.cover || 'https://via.placeholder.com/150'" :alt="book.title" class="cover" />
          <h3>{{ book.title }}</h3>
          <p>Автор: {{ book.author }}</p>
          <router-link :to="`/books/${book.id}`" class="link">Подробнее</router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const featuredBooks = ref([]);

onMounted(async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/book/');
    featuredBooks.value = response.data.slice(0, 3); // первые 3 книги
  } catch (error) {
    console.error('Ошибка загрузки книг:', error);
  }
});
</script>

<style scoped>
.home {
  text-align: center;
  padding: 2rem;
}
.btn {
  display: inline-block;
  margin: 1rem;
  padding: 0.75rem 1.5rem;
  background-color: #42b983;
  color: white;
  text-decoration: none;
  border-radius: 6px;
}
.featured {
  margin-top: 2rem;
}
.books-grid {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}
.book-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 1rem;
  width: 180px;
  text-align: left;
}
.cover {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 4px;
}
.link {
  display: block;
  margin-top: 0.5rem;
  color: #42b983;
  text-decoration: none;
}
</style>
