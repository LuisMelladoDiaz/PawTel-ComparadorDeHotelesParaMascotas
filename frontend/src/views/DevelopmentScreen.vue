<script setup>
import { ref } from 'vue';
import Navbar from '../components/Navbar.vue';
import FilterNavbar from '../components/FilterNavbar.vue';
import Footer from '../components/Footer.vue';
</script>

<template>
  <div>
    <Navbar />
    <FilterNavbar />

    <section class="hero bg-white text-terracota text-center py-20">
      <div class="max-w-7xl mx-auto px-5">
        <h1 class="text-4xl md:text-5xl font-bold mb-4">Bienvenido a la pantalla de desarrollo de Pawtel</h1>
        <p class="text-lg md:text-xl">Esta pantalla servirá principalmente para recopilar todos los links a las pantallas y componentes creados.</p>
        <p class="text-lg md:text-xl">Todas las pantallas que vayais desarrollando añadidlas a la seccion de Pantallas.</p>
      </div>
    </section>

    <section class="py-8 bg-gray-50">
      <div class="max-w-7xl mx-auto px-5 text-center">
        <h2 class="text-3xl font-bold">Explora las secciones</h2>
      </div>
    </section>

    <!-- ENLACES -->
    <section class="cards py-16 bg-gray-100">
      <div class="max-w-7xl mx-auto px-5 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 gap-8">
        <div class="card bg-white p-6 rounded-lg shadow-lg flex flex-col gap-2">
          <h2 class="text-xl font-semibold mb-4">Pantallas</h2>
          <router-link to="/templateScreen1" class="text-xl text-terracota hover:underline">Template Screen 1</router-link>
          <router-link to="/templateScreen2" class="text-xl text-terracota hover:underline">Template Screen 2</router-link>
          <router-link to="/hoteles" class="text-xl text-terracota hover:underline">Hotel List</router-link>
        </div>
        <div class="card bg-white p-6 rounded-lg shadow-lg flex flex-col gap-2">
          <h2 class="text-xl font-semibold mb-4">Componentes</h2>
          <router-link to="/componentes1" class="text-xl text-terracota hover:underline">Lista Componentes 1</router-link>
          <router-link to="/componentes2" class="text-xl text-terracota hover:underline">Lista Componentes 2</router-link>
        </div>
      </div>
    </section>

    <Footer />
  </div>
</template>

<style scoped>
@media (max-width: 900px) {
  .hero h1 {
    font-size: 2.5rem;
  }

  .hero p {
    font-size: 1rem;
  }

  .cards {
    padding-top: 8rem;
  }

  .card {
    padding: 1.5rem;
  }
}
</style>
