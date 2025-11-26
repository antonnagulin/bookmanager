<template>
  <div>
    <header class="header">
      <h1>📚 Библиотека</h1>
      <nav>
        <router-link to="/">Главная</router-link> |
        <router-link to="/books">Книги</router-link> |
        <router-link to="/readers">Читатели</router-link> |
        <router-link to="/loan">Выдать книгу</router-link> |
        <router-link to="/locations">Библиотеки</router-link>
      </nav>
      <button @click="toggleTheme" class="toggle-theme">
        {{ isDark ? 'Светлая тема' : 'Темная тема' }}
      </button>
    </header>

    <main class="main">
      <router-view />
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isDark = ref(document.body.classList.contains('dark'))

const toggleTheme = () => {
  document.body.classList.toggle('dark')
  isDark.value = document.body.classList.contains('dark')
  localStorage.setItem('darkMode', isDark.value)
}

// Проверяем сохранённую тему при загрузке
if (localStorage.getItem('darkMode') === 'true') {
  document.body.classList.add('dark')
  isDark.value = true
}
</script>

<style scoped>
.header {
  background: #42b983;
  color: white;
  padding: 1rem;
  text-align: center;
  position: relative;
}

.header a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

.main {
  padding: 2rem;
}

/* Кнопка переключения темы */
.toggle-theme {
  position: absolute;
  right: 1rem;
  top: 1rem;
  padding: 6px 12px;
  border: none;
  border-radius: 6px;
  background-color: #ffffffcc;
  color: #333;
  cursor: pointer;
  font-weight: 600;
  transition: 0.2s ease;
}

.toggle-theme:hover {
  opacity: 0.85;
}

/* Темная тема для хедера */
body.dark .header {
  background: #1f1f1f;
}

body.dark .toggle-theme {
  background-color: #6366f1;
  color: white;
}
</style>
