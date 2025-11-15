<!-- src/components/AddBookForm.vue -->
<template>
  <div class="form">
    <h3>Добавить книгу</h3>
    <input v-model="book.title" placeholder="Название" class="input" />
    <input v-model="book.author" placeholder="Автор" class="input" />
    <input v-model="book.total_copies" type="number" placeholder="Всего экземпляров" class="input" />
    <button @click="createBook" class="btn">Добавить</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const book = ref({
  title: '',
  author: '',
  total_copies: 1,
  available_copies: 1
})

const createBook = async () => {
  try {
    await axios.post('http://127.0.0.1:8000/book/', book.value)
    alert('Книга добавлена!')
    book.value = { title: '', author: '', total_copies: 1, available_copies: 1 }
    // Можно отправить событие родителю, чтобы обновить список
  } catch (error) {
    alert('Ошибка при добавлении книги')
    console.error(error)
  }
}
</script>

<style scoped>
.form { margin-bottom: 2rem; }
.input {
  display: block;
  width: 100%;
  max-width: 400px;
  margin: 0.5rem 0;
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 6px;
}
.btn {
  background: #42b983;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 6px;
  cursor: pointer;
}
</style>
