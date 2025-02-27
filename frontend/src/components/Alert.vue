<template>
  <div
    v-if="type"
    :class="[ 
      'p-4 rounded-lg text-white', 
      type === 'success' ? 'bg-oliva' :
      type === 'error' ? 'bg-terracota' :
      type === 'info' ? 'bg-azul-suave' : 'bg-gray-500',
      'fixed botom-4 left-4 z-50',
    ]"
  >
    <slot></slot>
  </div>
</template>

<script setup>
defineProps({
  type: { type: String, required: true }
});
</script>

<style scoped>
/* Aquí no es necesario añadir más estilos, ya que el posicionamiento está manejado con las clases */
</style>
