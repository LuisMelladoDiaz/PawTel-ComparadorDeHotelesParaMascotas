<template>
    <div>
        <Navbar />
        <FilterNavbar />

        <div class="max-w-7xl mx-auto px-5">

            Aquí va el contenido

        </div>

        <Footer />
    </div>
</template>

<script setup>
import { ref } from 'vue';
import Navbar from '../components/Navbar.vue';
import NavbarTerracota from '../components/NavbarTerracota.vue';
import FilterNavbar from '../components/FilterNavbar.vue';
import Footer from '../components/Footer.vue';
</script>

<style scoped>
/* Estilos adicionales */
</style>