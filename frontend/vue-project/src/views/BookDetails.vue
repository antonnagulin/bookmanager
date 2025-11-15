<!-- src/views/BookDetails.vue -->
<template>
  <div v-if="book" class="book-details">
    <button @click="$router.back()" class="back-btn">← Назад</button>
    <div class="book-info">
      <img :src="book.cover || 'https://via.placeholder.com/200'" :alt="book.title" class="cover" />
      <div class="text">
        <h1>{{ book.title }}</h1>
        <p><strong>Автор:</strong> {{ book.author }}</p>
        <p><strong>Год:</strong> {{ book.year }}</p>
        <p><strong>Жанр:</strong> {{ book.genre }}</p>
        <p><strong>Описание:</strong> {{ book.description || 'Нет описания' }}</p>
      </div>
    </div>
  </div>
  <div v-else class="loading">
    Загрузка...
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';

const route = useRoute();
const book = ref(null);

onMounted(async () => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/book/${route.params.id}/`);
    book.value = response.data;
  } catch (error) {
    console.error('Книга не найдена:', error);
    book.value = null;
  }
});
</script>

<style scoped>
.book-details {
  padding: 2rem;
}
.back-btn {
  margin-bottom: 1rem;
  padding: 0.5rem 1rem;
  background-color: #666;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.book-info {
  display: flex;
  gap: 2rem;
  align-items: flex-start;
  flex-wrap: wrap;
}
.cover {
  width: 200px;
  height: 300px;
  object-fit: cover;
  border-radius: 8px;
  border: 1px solid #ddd;
}
.text {
  flex: 1;
  min-width: 300px;
}
.text h1 {
  margin-top: 0;
  color: #333;
}
.loading {
  text-align: center;
  font-size: 1.2rem;
  color: #666;
}
</style>
