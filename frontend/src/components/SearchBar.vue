<template>
  <div class="search-bar flex items-center border border-terracota rounded-full">
    <!-- Icono de lupa -->
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20" class="search-icon">
      <circle cx="10" cy="10" r="7" fill="none" stroke="currentColor" stroke-width="2"/>
      <line x1="15" y1="15" x2="21" y2="21" stroke="currentColor" stroke-width="2"/>
    </svg>

    <!-- Campo de entrada -->
    <input
      type="text"
      placeholder="Buscar..."
      v-model="searchQuery"
      class="search-input px-2 py-1 outline-none w-full"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue';

const searchQuery = ref('');
</script>

<style scoped>

.search-bar {
  display: flex;
  align-items: center;
  border-radius: 10px;
  border: 1.5px solid #C36C6C;
  background-color: #fff;
}

.search-icon {
  margin-right: 8px;
  margin-left: 8px;
  color: #C36C6C; /* Color de la lupa terracota */
}

.search-input {
  border: none;
  width: 100%;
  font-size: 16px;
  color: #333;
  outline: none;
}

.search-input::placeholder {
  color: #aaa; /* Color gris para el placeholder */
}
</style>
