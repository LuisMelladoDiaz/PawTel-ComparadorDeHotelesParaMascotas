<script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter();

const goToPets = () => {
  router.push('/pets');
};

const goToHotels = () => {
  router.push('/hoteles');
};
</script>

<template>
  <div class="container">
    <h2 class="title">HomeView. Hey!</h2>
    <button class="styled-button" @click="goToPets">Go to Pets</button>
    <button class="styled-button hotels-btn" @click="goToHotels">Go to Hotels</button>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  text-align: center;
  font-family: Arial, sans-serif;
}

.title {
  font-size: 36px;
  color: #333;
  margin-bottom: 20px;
}

.styled-button {
  background-color: #007bff;
  color: white;
  font-size: 20px;
  padding: 10px 20px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s;
  margin: 10px;
}

.styled-button:hover {
  background-color: #0056b3;
  transform: scale(1.05);
}
</style>
