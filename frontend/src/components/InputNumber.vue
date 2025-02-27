<template>
  <div class="input-container">
    <label :for="id">{{ label }}</label>
    <div class="input-wrapper">
      <span v-if="icon" class="input-icon">{{ icon }}</span>
      <input 
        :id="id" 
        :value="modelValue" 
        @input="$emit('update:modelValue', $event.target.value)" 
        type="number" 
        :placeholder="placeholder" 
        class="input-number" 
        min="1"
      />
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';

defineProps({
  id: { type: String, required: true },
  label: { type: String, required: true },
  placeholder: { type: String, default: '' },
  modelValue: { type: Number, default: 1 },
  icon: { type: String, default: '' } // Nuevo prop para el ícono
});
</script>

<style scoped>
.input-container {
  display: flex;
  flex-direction: column;
}

.input-container label {
  color: #444;
  font-size: 14px;
}

.input-wrapper {
  display: flex;
  align-items: center;
  border: 1px solid #000;
  border-radius: 4px;
  background-color: white;
  width: 200px;
  height: 30px;
  padding-left: 8px;
}

.input-number {
  flex: 1;
  padding: 5px;
  border: none;
  outline: none;
  color: #888;
  font-size: 14px;
  background-color: white;
  height: 25px;
  width: 40px;
}

.input-icon {
  margin-right: 8px;
  color: #888;
}
</style>
