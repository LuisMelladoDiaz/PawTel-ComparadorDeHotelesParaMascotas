<template>
    <div class="container">
      <h2 class="title">Lista de Hoteles</h2>
      <div class="hotel-list">
        <div v-for="hotel in hoteles" :key="hotel.id" class="hotel-card">
          <img :src="hotel.imagen" alt="Hotel Image" class="hotel-img" />
          <h3>{{ hotel.nombre }}</h3>
          <p>{{ hotel.ciudad }}</p>
          <p class="price">Desde <strong>{{ hotel.precio }}€</strong> por noche</p>
          <button class="details-btn" @click="verDetalles(hotel.id)">Ver detalles</button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  
  // Datos ficticios
  const hoteles = [
    { id: 1, nombre: 'Hotel Sunset', ciudad: 'Madrid', precio: 120, imagen: 'https://source.unsplash.com/400x300/?hotel' },
    { id: 2, nombre: 'Grand Palace', ciudad: 'Barcelona', precio: 150, imagen: 'https://source.unsplash.com/400x300/?luxury-hotel' },
    { id: 3, nombre: 'Beach Resort', ciudad: 'Málaga', precio: 180, imagen: 'https://source.unsplash.com/400x300/?resort' },
  ];
  
  const verDetalles = (id: number) => {
    router.push(`/hotel/${id}`);
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 900px;
    margin: auto;
    text-align: center;
    font-family: Arial, sans-serif;
  }
  
  .title {
    font-size: 28px;
    margin-bottom: 20px;
  }
  
  .hotel-list {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
  }
  
  .hotel-card {
    background: white;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
    max-width: 250px;
  }
  
  .hotel-img {
    width: 100%;
    border-radius: 10px;
  }
  
  .price {
    font-size: 18px;
    color: #007bff;
  }
  
  .details-btn {
    background-color: #007bff;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-top: 10px;
  }
  
  .details-btn:hover {
    background-color: #0056b3;
  }
  </style>
  