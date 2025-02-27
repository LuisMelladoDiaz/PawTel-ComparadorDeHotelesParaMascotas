<script setup>
import { ref } from 'vue';
import InputText from './InputText.vue';
import InputNumber from './InputNumber.vue';

const city = ref('');
const dateRange = ref('');
const petCount = ref(1);

const onSearch = () => {
  console.log('Filtrando por:', { city: city.value, dateRange: dateRange.value, petCount: petCount.value });
};
</script>

<template>
  <div class="filter-navbar">
    <div class="filter-content">
      <InputText id="city" v-model="city" placeholder="Sevilla" icon="📍" />
      <InputText id="date-range" v-model="dateRange" placeholder="20 Junio - 23 Junio" icon="📅" />
      <InputNumber id="petCount" v-model="petCount" placeholder="2 perros" icon="🐶" />
      <button @click="onSearch" class="search-button">🔎 Buscar</button>
    </div>
  </div>
</template>

<style scoped>
.filter-navbar {
  background-color: #C36C6C;
  padding: 10px 20px;
  width: 100%;
}

.filter-content {
  width: 80%;
  height: 50px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
}

.search-button {
  background-color: white;
  color: #C36C6C;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  height: 30px;
  width: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  gap: 5px;
}

.search-button:hover {
  background-color: #D98C8C;
}
</style>
