<template>
  <nav class="navbar bg-white py-4 h-[70px] px-5">
    <div class="navbar-content max-w-7xl px-5 mx-auto flex justify-between items-center h-full">
      <!-- Ícono de menú para móviles -->
      <div class="menu-icon md:hidden flex flex-col items-end" @click="toggleMenu">
        <i class="fas fa-bars text-terracota text-3xl"></i>
      </div>
      
      <router-link to="/">
        <img src="../assets/pawtel-logo.png" alt="Logo" class="logo h-[50px]" />
      </router-link>

      <SearchBar class="search border-terracota" />

      <!-- Menú en pantallas grandes -->
      <div class="nav-links flex gap-6 no-underline text-terracota font-bold text-base hidden md:flex">
        <router-link to="/sobre_nosotros" class="hover:underline">Sobre Nosotros</router-link>
        <router-link to="/contacto" class="hover:underline">Contacto</router-link>
      </div>

      <!-- Botones de autenticación en pantallas grandes -->
      <div class="auth-buttons flex gap-5 text-white hidden md:flex">
        <button class="auth-button login bg-terracota hover:bg-terracota-dark rounded cursor-pointer px-4 py-2 border-none">Iniciar Sesión</button>
        <button class="auth-button sign-in bg-terracota hover:bg-terracota-dark rounded cursor-pointer px-4 py-2 border-none">Crear Cuenta</button>
      </div>


    </div>

    <!-- Menú desplegable en móvil -->
    <div v-if="isMenuOpen" class="mobile-menu md:hidden bg-white py-4 border-t-2 border-terracota shadow-lg rounded-b-lg">
      <div class="nav-links flex flex-col text-terracota font-bold text-base">
        <router-link to="/sobre_nosotros" class="hover:underline p-2">Sobre Nosotros</router-link>
        <router-link to="/contacto" class="hover:underline p-2">Contacto</router-link>
      </div>

      <!-- Botones de autenticación en el menú móvil -->
      <div class="auth-buttons flex flex-col gap-3 text-white mt-4">
        <button class="auth-button login bg-terracota hover:bg-terracota-dark rounded cursor-pointer px-4 py-2 border-none">Iniciar Sesión</button>
        <button class="auth-button sign-in bg-terracota hover:bg-terracota-dark rounded cursor-pointer px-4 py-2 border-none">Crear Cuenta</button>
      </div>
    </div>
  </nav>
</template>

<script>
import { ref } from 'vue';
import SearchBar from './SearchBar.vue';

export default {
  components: {
    SearchBar,
  },
  setup() {
    const isMenuOpen = ref(false);

    // Función para alternar el estado del menú
    const toggleMenu = () => {
      isMenuOpen.value = !isMenuOpen.value;
    };

    return { isMenuOpen, toggleMenu };
  },
};
</script>

<style scoped>
  @media (max-width: 900px) {
    .navbar-content {
      display: flex;
      justify-content: flex-start;
      align-items: center;
      width: 100%;
    }

    /* Menú desplegable en móvil */
    .mobile-menu {
      position: absolute;
      top: 70px;
      left: 0;
      right: 0;
      margin-left: 5px;
      margin-right: 5px;
      margin-top: 5px;
      border-color: #c36c6c;
      background-color: white;
      border: 2px solid #c36c6c ; /* Borde superior en terracota */
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Sombra suave */
      z-index: 10;
      padding: 20px;
      border-radius: 8px; /* Bordes redondeados */
      max-height: auto;
    }

    /* Estilo para los enlaces */
    .nav-links a {
      display: block;
      padding: 12px;
      font-size: 16px;
      color: #c36c6c ;
      font-weight: bold;
      text-decoration: none;
    }

    .nav-links a:hover {
      background-color: #f3f1f1;
      border-radius: 4px;
    }

    /* Estilos para el ícono de hamburguesa */
    .menu-icon span {
      transition: all 0.3s;
    }
    .menu-icon {
      margin-right: 10px;
      position: relative;
      right: 8px;
      top: 5px;
    }

    .search {
      width: 107px;
      position: absolute;
      right: 30px;
      top: 21px
    }
    .logo {
      height: 50px;
    }

  }
</style>
