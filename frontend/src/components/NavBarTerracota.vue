<template>
  <nav class="navbar bg-[#C36C6C] py-4">
    <div class="navbar-content max-w-7xl px-5 mx-auto flex justify-between items-center">
      <!-- Logo -->
      <router-link to="/home" class="logo">
        <img src="../assets/pawtel-logo-white.png" alt="Logo" />
      </router-link>

      <!-- Barra de búsqueda -->
      <SearchBar />

      <!-- Enlaces de navegación -->
      <div class="nav-links flex gap-6">
        <router-link to="/sobre_nosotros" class="nav-link">Sobre Nosotros</router-link>
        <router-link to="/contacto" class="nav-link">Contacto</router-link>
      </div>

      <!-- Botones de login y sign in -->
      <div class="auth-buttons flex gap-4">
        <button class="auth-button login">Iniciar Sesión</button>
        <button class="auth-button sign-in">Crear Cuenta</button>
      </div>
    </div>
  </nav>
</template>

<script>
import SearchBar from './SearchBar.vue'; // Importando el componente de la barra de búsqueda

export default {
  components: {
    SearchBar,
  },
};
</script>

<style scoped>

.navbar {
  background-color: #C36C6C;
  padding: 10px 20px;
  height: 60px;
}

.navbar-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100%;
}

.logo img {
  height: 40px;
}

.nav-links {
  display: flex;
  gap: 20px;
}

.nav-link {
  text-decoration: none;
  color: #fff; 
  font-weight: bold;
  font-size: 16px;
}

.nav-link:hover {
  text-decoration: underline;
}

.auth-buttons .auth-button {
  background-color: #fff;
  color: #C36C6C;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-left: 10px;
}

.auth-buttons .auth-button:hover {
  background-color: #F4EDEA;
}

.search-bar input:focus,
.nav-link:hover {
  outline: none;
}
</style>
