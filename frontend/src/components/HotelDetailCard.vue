<script setup>
import { defineProps } from 'vue';
import Button from '../components/Button.vue';

defineProps({
  image: { type: String, required: true },
  name: { type: String, required: true },
  location: { type: String, required: true },
  details: { type: Array, required: true },
  rating: { type: Number, required: true },
  price: { type: String, required: true },
  reviews: { type: Array, required: true },
  imageGallery: { type: Array, required: true },
  description: { type: String, required: true }
});
</script>

<template>
  <div class="hotel-detail-container max-w-[1000px] mx-auto p-5 border rounded-lg shadow-lg">
    
    <!-- Banner con Nombre y Ubicación -->
    <div class="bg-terracota text-white text-center py-4 rounded-t-lg">
      <h2 class="text-2xl font-bold">{{ name }}</h2>
      <p class="text-lg">{{ location }}</p>
    </div>

    <div class="flex flex-wrap gap-4 mt-4">
      <!-- Columna Izquierda: Valoración y Reseña -->
      <div class="flex-1 min-w-[250px]">
        <div class="rating-container text-center p-3 bg-gray-100 rounded-lg">
          <span class="text-3xl font-bold text-terracota">{{ rating }}</span>
          <p class="text-sm text-gray-600">Basado en 120 reseñas</p>
        </div>
        <div class="review bg-gray-50 p-4 mt-4 rounded-lg shadow-sm">
          <p class="font-bold">Usuario1</p>
          <p class="text-sm italic">"Un lugar increíble, el servicio es excelente y las instalaciones son de primera calidad."</p>
        </div>
      </div>

      <!-- Columna Central: Galería de Imágenes -->
      <div class="flex-1 min-w-[300px]">
        <div class="image-gallery grid grid-cols-2 gap-2">
          <img v-for="(img, index) in imageGallery" :key="index" :src="img" alt="Hotel" class="w-full h-32 object-cover rounded-lg" />
        </div>
      </div>

      <!-- Columna Derecha: Reservas y Descripción -->
      <div class="flex-1 min-w-[250px] flex flex-col items-center text-center">
        <Button type="add" class="w-full">Reservar</Button>
        <p class="text-lg font-bold text-terracota mt-4 w-full">{{ price }}</p>
        <p class="text-sm text-gray-700 mt-2 w-full">{{ description }}</p>
        <ul class="text-sm text-gray-700 mt-2 w-full">
            <li v-for="(detail, index) in details" :key="index">✔ {{ detail }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>
.hotel-detail-container {
  background: white;
}
</style>