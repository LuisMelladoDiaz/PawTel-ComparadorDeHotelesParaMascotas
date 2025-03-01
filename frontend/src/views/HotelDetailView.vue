<script setup>
import { ref } from 'vue';
import { useRoute } from 'vue-router';
import Navbar from '../components/Navbar.vue';
import FilterNavbar from '../components/FilterNavbar.vue';
import Footer from '../components/Footer.vue';
import HotelDetailCard from '../components/HotelDetailCard.vue';

const route = useRoute();
const hotel = ref({
  image: '/src/assets/foto1.jpg',
  name: 'Hotel Ejemplo',
  location: '📍'+'Madrid, España',
  details: ['WiFi gratis', 'Desayuno incluido', 'Piscina', 'Gimnasio'],
  rating: 4.5,
  price: '120€/noche',
  imageGallery: [
    '/src/assets/foto1.jpg',
    '/src/assets/foto2.jpg',
    '/src/assets/foto1.jpg',
    '/src/assets/foto2.jpg'
  ],
  description: 'Un hotel increíble con todas las comodidades que necesitas para unas vacaciones perfectas.'
});
</script>

<template>
  <div>
    <Navbar />
    <FilterNavbar />

    <!-- Barra de navegación entre pestañas -->
    <div class="bg-white shadow-md py-2 flex justify-center gap-6 text-black text-lg border-b">
      <a href="#" class="hover:underline">Vista General</a>
      <a href="#" class="hover:underline">Información y Precios</a>
      <a href="#" class="hover:underline">Servicios</a>
      <a href="#" class="hover:underline">Requisitos</a>
      <a href="#" class="hover:underline">A Tener en Cuenta</a>
      <a href="#" class="hover:underline">Opiniones de Clientes</a>
    </div>

    <div class="max-w-7xl mx-auto px-5 py-10">
      <HotelDetailCard 
        :image="hotel.image"
        :name="hotel.name"
        :location="hotel.location"
        :details="hotel.details"
        :rating="hotel.rating"
        :price="hotel.price"
        :imageGallery="hotel.imageGallery"
        :description="hotel.description"
      />
    </div>
    <Footer />
  </div>
</template>

<style scoped>
@media (max-width: 900px) {
  .text-lg {
    font-size: 1rem;
  }
}
</style>