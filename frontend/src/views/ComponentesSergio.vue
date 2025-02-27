<script setup lang="ts">
import { useGetRandomPets } from '../data-layer/pets';
import { ref } from 'vue';

const count = ref<number>(3);


const { data: pets, isLoading, error } = useGetRandomPets(count);


const setCount = (event: Event) => {
  const target = event.target as HTMLInputElement;
  const newCount = parseInt(target.value, 10);
  if (!isNaN(newCount) && newCount > 0) {
    count.value = newCount;
  }
};
</script>

<template>
  <div class="container">
    <div class="input-container">
      <label for="count">Count of pets:</label>
      <input id="count" type="number" :value="count" @input="setCount" min="1" />
    </div>
    <h2 class="title">Pets</h2>
    
    <p v-if="isLoading" class="loading-text">Loading...</p>
    <p v-else-if="error" class="error-text">{{ error }}</p>
    
    <div v-else class="grid">
      <div v-for="pet in pets" :key="pet.id" class="pet-card">
        <img :src="pet.image" :alt="pet.name" class="pet-image"/>
        <p class="pet-name">{{ pet.name }}</p>
      </div>
    </div>


  </div>
</template>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
  font-family: Arial, sans-serif;
}

.title {
  color: blue;
  font-size: 36px;
  margin-bottom: 20px;
}

.loading-text {
  font-size: 24px;
  font-weight: bold;
}

.error-text {
  color: red;
  font-size: 24px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 20px;
  justify-content: center;
  margin: 20px 0;
}

.pet-card {
  background: #f9f9f9;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
}

.pet-card:hover {
  transform: scale(1.05);
}

.pet-image {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
}

.pet-name {
  font-size: 18px;
  font-weight: bold;
  margin-top: 10px;
}

.input-container {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}

input {
  width: 60px;
  height: 35px;
  font-size: 18px;
  text-align: center;
  border: 1px solid black;
  border-radius: 5px;
  padding: 5px;
}
</style>
