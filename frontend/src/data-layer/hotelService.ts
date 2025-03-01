import axios from 'axios';

export const getHotelById = async (id: number) => {
  try {
    const response = await axios.get(`http://localhost:5000/hotels/${id}`);
    return response.data;
  } catch (error) {
    console.error('Error al obtener el hotel:', error);
    return null;
  }
};
