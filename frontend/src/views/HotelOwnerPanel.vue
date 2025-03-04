<template>
  <div class="flex flex-col min-h-screen">
    <NavbarTerracota />

    <div class="max-w-7xl mx-auto px-5 w-full flex flex-col items-center flex-grow justify-center mt-8">

      <!-- Fila superior -->
      <div class="flex justify-between items-center bg-terracota text-white px-4 py-2 rounded-t-lg w-full mb-1">
        <span class="font-semibold">Gestión de Hoteles</span>
        <button @click="openModal" class="flex items-center text-white bg-terracota hover:bg-terracota-dark rounded-full px-4 py-2">
          <i class="fas fa-plus mr-2"></i> Añadir Nuevo
        </button>
      </div>
      
      <!-- Tabla de hoteles con estilo modernizado -->
      <div class="overflow-x-auto w-full">
        <table class="w-full border-collapse shadow-md rounded-b-lg overflow-hidden mb-4">
          <thead>
            <tr class="bg-white text-left">
              <th class="px-4 py-2">Nombre</th>
              <th class="px-4 py-2">Dirección</th>
              <th class="px-4 py-2">Ciudad</th>
              <th class="px-4 py-2">Descripción</th>
              <th class="px-4 py-2 text-center">Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(hotel, index) in paginatedHotels" :key="hotel.id" :class="index % 2 === 0 ? 'bg-gray-100' : 'bg-white'">
              <td class="px-4 py-2">{{ hotel.name }}</td>
              <td class="px-4 py-2">{{ hotel.address }}</td>
              <td class="px-4 py-2">{{ hotel.city }}</td>
              <td class="px-4 py-2">{{ hotel.description }}</td>
              <td class="px-4 py-2 text-center flex justify-center gap-2">
                <button @click="openModal(hotel)" class="text-oliva hover:text-oliva-dark">
                  <i class="fas fa-edit"></i>
                </button>
                <button @click="deleteHotel(hotel.id)" class="text-terracota hover:text-terracota-dark">
                  <i class="fas fa-trash"></i>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      
      <!-- Información de paginación -->
      <div class="flex justify-between w-full mt-4 flex-col md:flex-row">
        <span class="text-gray-600">Mostrando {{ paginatedHotels.length }} hoteles de {{ hotels.length }}</span>
        <div class="flex gap-2 mt-2 md:mt-0">
          <button @click="prevPage" :disabled="currentPage === 1" class="px-3 py-1 bg-gray-200 rounded disabled:opacity-50">← Anterior</button>
          <button v-for="page in totalPages" :key="page" @click="currentPage = page" 
                  class="px-3 py-1" :class="{'bg-gray-300': currentPage === page, 'bg-gray-200': currentPage !== page}">
            {{ page }}
          </button>
          <button @click="nextPage" :disabled="currentPage === totalPages" class="px-3 py-1 bg-gray-200 rounded disabled:opacity-50">Siguiente →</button>
        </div>
      </div>

      <!-- Línea estilística -->
      <div class="w-full mt-4 border-t border-gray-300"></div>

    </div>

    <Footer />
    
    <!-- Modal para añadir/editar hotel -->
    <div v-if="modalOpen" class="fixed inset-0 flex items-center justify-center bg-gray-900 bg-opacity-50">
      <div class="bg-white p-6 rounded-lg w-1/3">
        <h2 class="text-xl font-bold mb-4">{{ isEditing ? 'Editar Hotel' : 'Añadir Hotel' }}</h2>
        <input v-model="hotelData.name" placeholder="Nombre" class="w-full p-2 mb-2 border rounded" />
        <input v-model="hotelData.address" placeholder="Dirección" class="w-full p-2 mb-2 border rounded" />
        <input v-model="hotelData.city" placeholder="Ciudad" class="w-full p-2 mb-2 border rounded" />
        <textarea v-model="hotelData.description" placeholder="Descripción" class="w-full p-2 mb-2 border rounded"></textarea>
        <div class="flex justify-end gap-2">
          <Button type="accept" @click="saveHotel">Guardar</Button>
          <Button type="reject" @click="modalOpen = false">Cancelar</Button>
        </div>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref, computed } from 'vue';
import NavbarTerracota from '../components/NavbarTerracota.vue';
import Footer from '../components/Footer.vue';
import Button from '../components/Button.vue';

const hotels = ref([
  { id: 1, name: 'Hotel Sol', address: 'Calle 123', city: 'Madrid', description: 'Hotel con vistas al mar.' },
  { id: 2, name: 'Hotel Luna', address: 'Avenida 456', city: 'Barcelona', description: 'Hotel en el centro de la ciudad.' },
  { id: 3, name: 'Hotel Estrella', address: 'Calle 789', city: 'Sevilla', description: 'Cerca de la catedral.' },
  { id: 4, name: 'Hotel Noche', address: 'Calle 321', city: 'Granada', description: 'Vista a la Alhambra.' },
  { id: 5, name: 'Hotel Amanecer', address: 'Av. Sol 12', city: 'Valencia', description: 'Junto a la playa.' },
  { id: 6, name: 'Hotel Brisa', address: 'Calle Mar 15', city: 'Málaga', description: 'Ambiente costero.' },
  { id: 7, name: 'Hotel Cielo', address: 'Paseo Azul', city: 'Bilbao', description: 'Vistas impresionantes.' }
]);

const modalOpen = ref(false);
const isEditing = ref(false);
const hotelData = ref({ name: '', address: '', city: '', description: '' });
const currentPage = ref(1);
const itemsPerPage = 5;

const totalPages = computed(() => Math.ceil(hotels.value.length / itemsPerPage));

const paginatedHotels = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  return hotels.value.slice(start, start + itemsPerPage);
});

const openModal = (hotel = null) => {
  hotelData.value = hotel ? { ...hotel } : { name: '', address: '', city: '', description: '' };
  isEditing.value = !!hotel;
  modalOpen.value = true;
};

const saveHotel = () => {
  if (isEditing.value) {
    const index = hotels.value.findIndex(h => h.id === hotelData.value.id);
    if (index !== -1) hotels.value[index] = { ...hotelData.value };
  } else {
    hotelData.value.id = hotels.value.length + 1;
    hotels.value.push({ ...hotelData.value });
  }
  modalOpen.value = false;
};

const deleteHotel = (id) => {
  if (confirm('¿Estás seguro de eliminar este hotel?')) {
    hotels.value = hotels.value.filter(h => h.id !== id);
  }
};

const prevPage = () => {
  if (currentPage.value > 1) currentPage.value--;
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) currentPage.value++;
};
</script>

<style scoped>
button {
  transition: background 0.3s ease;
}

button:hover {
  cursor: pointer;
}

.bg-terracota-dark {
  background-color: #d57c1a; /* Este color debe ser un tono más oscuro de terracota */
}

.flex-grow {
  flex-grow: 1;
}
</style>