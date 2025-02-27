from django.test import TestCase
from hotels.models import Hotel
from hotelOwners.models import HotelOwner 
from django.core.exceptions import ValidationError

class HotelModelTest(TestCase):

    def setUp(self):
        self.owner = HotelOwner.objects.create_user(
            username="hotelowner1",
            first_name="John",
            last_name="Doe",
            email="owner@example.com",
            phone="+34987654321",
            password="securepassword123"
        )

    def test_create_valid_hotel(self):
        hotel = Hotel.objects.create(
            name="Barceló",
            address="Calle Principal 123",
            city="Madrid",
            description="Un hotel de prueba con buenas vistas.",
            hotel_owner=self.owner
        )
        self.assertEqual(hotel.name, "Barceló")
        self.assertEqual(hotel.address, "Calle Principal 123")
        self.assertEqual(hotel.city, "Madrid")
        self.assertEqual(hotel.description, "Un hotel de prueba con buenas vistas.")
        self.assertEqual(hotel.hotel_owner, self.owner)  

    def test_create_hotel_without_owner(self):
        hotel = Hotel(
            name="Hotel Sin Dueño",
            address="Calle Falsa 123",
            city="Madrid",
            description="Un hotel sin dueño",
            hotel_owner=None  
        )
        with self.assertRaises(ValidationError):
            hotel.full_clean()

    def test_create_hotel_invalid_name(self):
        hotel = Hotel(
            name="",
            address="Calle Principal 123",
            city="Madrid",
            description="Un hotel de prueba.",
            hotel_owner=self.owner
        )
        with self.assertRaises(ValidationError):
            hotel.full_clean()

    def test_create_hotel_invalid_address(self):
        hotel = Hotel(
            name="Hotel Sirena",
            address="",
            city="Sevilla",
            description="Hotel muy chill",
            hotel_owner=self.owner
        )
        with self.assertRaises(ValidationError):
            hotel.full_clean()

    def test_create_hotel_invalid_city(self):
        hotel = Hotel(
            name="Hotel Sevilla",
            address="Avenida del Mar 22",
            city="",
            description="Hotel de lujo",
            hotel_owner=self.owner
        )
        with self.assertRaises(ValidationError):
            hotel.full_clean()

    def test_create_hotel_invalid_description(self):
        hotel = Hotel(
            name="Hotel 3 lunas",
            address="Calle de la Luna 5",
            city="Valencia",
            description="",
            hotel_owner=self.owner
        )
        with self.assertRaises(ValidationError):
            hotel.full_clean()