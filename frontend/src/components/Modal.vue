<template>
  <div v-if="isOpen" class="fixed inset-0 bg-black bg-opacity-30 flex justify-center items-center">
    <div class="bg-white p-6 rounded-lg w-1/3">
      <!-- Título y botón de cerrar -->
      <div class="flex justify-between items-center mb-4">
        <h3 class="text-lg font-semibold" v-if="title">{{ title }}</h3>
        <button @click="emitClose" class="text-gray-500 hover:text-black text-xl">&times;</button>
      </div>

      <!-- Contenido del modal -->
      <div class="mb-6">
        <slot></slot>
      </div>

      <!-- Botones de acción -->
      <div class="flex justify-end gap-4">
        <Button type="reject" @click="handleReject">Rechazar</Button>
        <Button type="accept" @click="handleAccept">Aceptar</Button>
      </div>
    </div>
  </div>
</template>

<script setup>
import Button from './Button.vue';

// Definir las props que el componente recibirá
const props = defineProps({
  isOpen: { type: Boolean, required: true },
  title: { type: String, default: '' }
});

// Emite los eventos para el componente Modal
const emit = defineEmits(['close', 'accept', 'reject']);

// Métodos para manejar las acciones del modal
const emitClose = () => {
  emit('close'); // Cierra el modal
};

const handleAccept = () => {
  emitClose();   // Cierra el modal
  emit('accept'); // Emite el evento de aceptar
};

const handleReject = () => {
  emitClose();   // Cierra el modal
  emit('reject'); // Emite el evento de rechazar
};
</script>

<style scoped>
div {
  font-family: var(--font-complementario);
}
</style>
