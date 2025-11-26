import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Подключаем CSS с темами
import './assets/css/theme.css'

const app = createApp(App)
app.use(router)
app.mount('#app')

// Проверка, нужно ли включить темную тему по умолчанию
// Например, можно сохранять в localStorage
const isDark = localStorage.getItem('darkMode') === 'true'
if (isDark) {
  document.body.classList.add('dark')
}

// Функция для переключения темы (можно вызывать из любого компонента)
app.config.globalProperties.$toggleTheme = () => {
  document.body.classList.toggle('dark')
  const dark = document.body.classList.contains('dark')
  localStorage.setItem('darkMode', dark)
}
