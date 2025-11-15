<template>
  <div class="page">
    <h1 class="title">📚 Список книг</h1>
    <button @click="openModal()" class="btn add">➕ Добавить книгу</button>

    <div v-if="books.length" class="table-wrapper">
      <table class="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Обложка</th>
            <th>Название</th>
            <th>Автор</th>
            <th>Год</th>
            <th>Жанр</th>
            <th>Доступно / Всего</th>
            <th class="actions-col">Действия</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="book in books" :key="book.id">
            <td>{{ book.id }}</td>
            <td>
              <img v-if="book.cover" :src="book.cover" class="cover" />
            </td>
            <td>{{ book.title }}</td>
            <td>{{ book.author }}</td>
            <td>{{ book.year }}</td>
            <td>{{ book.genre }}</td>
            <td>{{ book.available_copies }} / {{ book.total_copies }}</td>
            <td>
              <button @click="openModal(book)" class="btn edit">✏️</button>
              <button @click="deleteBook(book.id)" class="btn delete">🗑️</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-else class="empty"><p>Книг пока нет</p></div>

    <!-- Модальное окно -->
    <div v-if="modalOpen" class="modal-overlay">
      <div class="modal">
        <h2 class="modal-title">{{ editingBook ? 'Редактировать книгу' : 'Добавить книгу' }}</h2>

        <input v-model="form.title" placeholder="Название" class="input" @input="searchBook" />
        <ul v-if="suggestions.length" class="suggestions">
          <li v-for="s in suggestions" :key="s.title + s.author" @click="fillBook(s)">
            <img v-if="s.cover" :src="s.cover" class="mini-cover" /> {{ s.title }} — {{ s.author }} ({{ s.year }})
          </li>
        </ul>

        <input v-model="form.author" placeholder="Автор" class="input" />
        <input v-model="form.year" type="number" placeholder="Год" class="input" />
        <input v-model="form.genre" placeholder="Жанр" class="input" />
        <textarea v-model="form.description" placeholder="Описание" class="input"></textarea>
        <input v-model="form.cover" placeholder="URL обложки" class="input" />
        <input v-model.number="form.total_copies" type="number" placeholder="Всего копий" class="input" />
        <input v-model.number="form.available_copies" type="number" placeholder="Доступно копий" class="input" />

        <div class="modal-buttons">
          <button @click="submitBook" class="btn save">{{ editingBook ? 'Сохранить' : 'Добавить' }}</button>
          <button @click="closeModal" class="btn cancel">Отмена</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const books = ref([])
const modalOpen = ref(false)
const editingBook = ref(null)
const form = ref({
  title: '', author:'', year:'', genre:'', description:'', cover:'', total_copies:1, available_copies:1
})
const suggestions = ref([])

const loadBooks = async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/book/')
    books.value = res.data
  } catch(e){ console.error(e) }
}

const openModal = (book=null) => {
  modalOpen.value = true
  if(book){
    editingBook.value = book
    form.value = { ...book }
  } else {
    editingBook.value = null
    form.value = { title:'', author:'', year:'', genre:'', description:'', cover:'', total_copies:1, available_copies:1 }
  }
}

const closeModal = () => {
  modalOpen.value = false
  form.value = { title:'', author:'', year:'', genre:'', description:'', cover:'', total_copies:1, available_copies:1 }
  suggestions.value = []
  editingBook.value = null
}

const submitBook = async () => {
  try {
    if(editingBook.value){
      await axios.put(`http://127.0.0.1:8000/book/${editingBook.value.id}/`, form.value)
      alert("Книга обновлена!")
    } else {
      await axios.post("http://127.0.0.1:8000/book/", form.value)
      alert("Книга добавлена!")
    }
    closeModal()
    await loadBooks()
  } catch(e){ alert("Ошибка при сохранении") }
}

const deleteBook = async (id) => {
  if(!confirm("Удалить книгу?")) return
  try { await axios.delete(`http://127.0.0.1:8000/book/${id}/`); await loadBooks() } 
  catch(e){ alert("Ошибка при удалении") }
}

const searchBook = async () => {
  if(form.value.title.length < 3){ suggestions.value = []; return }
  try {
    const res = await axios.get("http://127.0.0.1:8000/book/autocomplete/", { params: { title: form.value.title } })
    suggestions.value = res.data
  } catch(e){ console.error(e) }
}

const fillBook = (bookData) => {
  form.value.title = bookData.title
  form.value.author = bookData.author
  form.value.year = bookData.year || ''
  form.value.genre = bookData.genre || ''
  form.value.description = bookData.description || ''
  form.value.cover = bookData.cover || ''
  form.value.total_copies = bookData.total_copies || 1
  form.value.available_copies = bookData.available_copies || 1
  suggestions.value = []
}

onMounted(loadBooks)
</script>

<style scoped>
.page { max-width: 1000px; margin:auto; padding:2rem; }
.title { text-align:center; font-size:2rem; margin-bottom:1rem; }

.add { background:#2e7d32; color:white; margin-bottom:1rem; padding:0.6rem 1rem; border:none; border-radius:6px; cursor:pointer; font-weight:bold }
.add:hover { transform:scale(1.05); }

.table-wrapper { overflow-x:auto; border-radius:10px; box-shadow:0 2px 8px rgba(0,0,0,0.1); }
.table { width:100%; border-collapse:collapse; background:white; table-layout: fixed; }
.table th, .table td { padding:0.75rem 1rem; border-bottom:1px solid #e5e5e5; text-align:left; vertical-align:middle; }
.table th { background:#f5f5f5; font-weight:bold; }
.table tr:hover { background:#f9fafc }

.cover { width:50px; height:auto; border-radius:4px; }
.mini-cover { width:30px; height:auto; margin-right:0.5rem; vertical-align:middle; }

.actions-col { width:120px; }
.actions { display:flex; justify-content:flex-end; align-items:center; gap:0.5rem; }

.btn { border:none; padding:0.4rem 0.7rem; font-size:0.9rem; cursor:pointer; border-radius:6px; transition:0.2s ease }
.edit { background:#1976d2; color:white }
.delete { background:#d32f2f; color:white }
.save { background:#42b983; color:white }
.cancel { background:#b0bec5 }

.modal-overlay { position:fixed; inset:0; background:rgba(0,0,0,0.45); display:flex; justify-content:center; align-items:center; animation:fade 0.2s ease }
.modal { background:white; padding:2rem; border-radius:12px; width:500px; box-shadow:0 4px 16px rgba(0,0,0,0.2); animation:pop 0.25s ease }
.modal-title { margin-bottom:1rem }
.input { width:100%; margin-bottom:0.8rem; padding:0.7rem; border-radius:6px; border:1px solid #ccc; }
textarea.input { resize:vertical; height:80px; }
.modal-buttons { display:flex; justify-content:space-between; margin-top:1rem }

.suggestions { border:1px solid #ccc; max-height:150px; overflow:auto; margin-top:-0.5rem; margin-bottom:0.5rem; border-radius:6px; background:white; list-style:none; padding:0 }
.suggestions li { padding:0.5rem; cursor:pointer; display:flex; align-items:center; }
.suggestions li:hover { background:#f0f0f0 }

.empty { text-align:center; margin-top:2rem; color:#777 }

@keyframes fade { from{opacity:0} to{opacity:1} }
@keyframes pop { from{opacity:0; transform:scale(0.9)} to{opacity:1; transform:scale(1)} }
</style>
