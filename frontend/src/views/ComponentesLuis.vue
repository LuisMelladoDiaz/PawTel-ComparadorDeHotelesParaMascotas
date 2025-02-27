<template>
  <div>
    <Navbar />
    <Navbar-Terracota/>
    <FilterNavbar />

    <div class="w-4/5 mx-auto">
      
      <div class="p-6 flex flex-col gap-6 items-center">
        <!-- Botones de acción -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
          <Button type="accept">Aceptar</Button>
          <Button type="reject">Rechazar</Button>
          <Button type="add">Añadir</Button>
          <Button type="edit">Editar</Button>
        </div>

        <!-- Botones para testear modales y alertas -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
          <Button type="add" @click="showModal = true">Abrir Modal</Button>
          <Button type="accept" @click="showAlert = 'success'">Mostrar Éxito</Button>
          <Button type="reject" @click="showAlert = 'error'">Mostrar Error</Button>
          <Button type="edit" @click="showAlert = 'info'">Mostrar Info</Button>
        </div>

        <!-- Inputs de ejemplo -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 w-full justify-center">
          <!-- Input de texto -->
          <div class="flex flex-col gap-2 items-center">
            <label for="textInput" class="text-lg">Ejemplo de Input de Texto</label>
            <InputText id="textInput" placeholder="Escribe algo..." />
          </div>
          <!-- Input numérico -->
          <div class="flex flex-col gap-2 items-center">
            <label for="numberInput" class="text-lg">Ejemplo de Input Numérico</label>
            <InputNumber id="numberInput" placeholder="Número" />
          </div>
          
        </div>
        
      </div>
    </div>

    <Footer />

    <!-- Modal -->
    <Modal :isOpen="showModal" title="Ejemplo Modal" @close="showModal = false">
      <p>Este es un modal de prueba.</p>
    </Modal>

    <!-- Alertas -->
    <Alert v-if="showAlert" :type="showAlert">Este es un mensaje de {{ showAlert }}.</Alert>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import Navbar from '../components/Navbar.vue';
import NavbarTerracota from '../components/NavbarTerracota.vue';
import FilterNavbar from '../components/FilterNavbar.vue';
import Footer from '../components/Footer.vue';
import Button from '../components/Button.vue';
import Modal from '../components/Modal.vue';
import Alert from '../components/Alert.vue';
import InputText from '../components/InputText.vue';  // Importando el componente InputText
import InputNumber from '../components/InputNumber.vue';  // Importando el componente InputNumber

const showModal = ref(false);
const showAlert = ref('');
</script>

<style scoped>
/* Estilos adicionales */
input {
  font-family: var(--font-complementario);
}
</style>
