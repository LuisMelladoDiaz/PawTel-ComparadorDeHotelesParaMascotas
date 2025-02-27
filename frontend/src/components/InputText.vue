<template>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
  <div class="input-container">
    <label :for="id">{{ label }}</label>
    <div class="input-wrapper">
      <span v-if="icon" class="input-icon">{{ icon }}</span>
      <input 
        :id="id" 
        :value="modelValue" 
        @input="$emit('update:modelValue', $event.target.value)" 
        type="text" 
        :placeholder="placeholder" 
        class="input-text" 
      />

      <span 
        v-if="modelValue" 
        class="clear-icon font-bold" 
        @click="$emit('update:modelValue', '')"
      >
        <i class="fas fa-times"></i>
      </span>

    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';

defineProps({
  id: { type: String, required: true },
  label: { type: String, required: true },
  placeholder: { type: String, default: '' },
  modelValue: { type: String, default: '' },
  icon: { type: String, default: '' }
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
  position: relative;
  padding-left: 8px;
}

.input-text {
  flex: 1;
  padding: 5px 25px 5px 5px;
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

.clear-icon {
  position: absolute;
  right: 8px;
  cursor: pointer;
  margin-right: 8px;
  color: #C36C6C;
}

.clear-icon i {
  font-size: 14px;
}

.clear-icon:hover i {
  color: #555;
}
</style>
