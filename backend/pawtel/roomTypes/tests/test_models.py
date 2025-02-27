from django.test import TestCase
from roomTypes.models import RoomType, PetType
from hotels.models import Hotel
from hotelOwners.models import HotelOwner
from django.core.exceptions import ValidationError

class RoomTypeModelTest(TestCase):

    def setUp(self):
        self.owner = HotelOwner.objects.create_user(
            username="hotelowner1",
            first_name="John",
            last_name="Doe",
            email="owner@example.com",
            phone="+34987654321",
            password="securepassword123"
        )

        self.hotel = Hotel.objects.create(
            name="Hotel Test",
            address="Calle Principal 123",
            city="Madrid",
            description="Un hotel de prueba.",
            hotel_owner=self.owner  
        )

    def test_create_valid_roomtype(self):
        room_type = RoomType.objects.create(
            hotel=self.hotel,
            name="Suite Deluxe",
            description="Una habitación lujosa con vista al mar.",
            capacity=2,
            price_per_night=150.00,
            pet_type=PetType.DOG
        )
        self.assertEqual(room_type.name, "Suite Deluxe")
        self.assertEqual(room_type.description, "Una habitación lujosa con vista al mar.")
        self.assertEqual(room_type.capacity, 2)
        self.assertEqual(room_type.price_per_night, 150.00)
        self.assertEqual(room_type.pet_type, PetType.DOG)
        self.assertEqual(room_type.hotel, self.hotel)
        self.assertEqual(room_type.hotel.hotel_owner, self.owner)

    def test_create_roomtype_without_hotel(self):
        room_type = RoomType(
            hotel=None, 
            name="Suite Lujo",
            description="Habitación grande",
            capacity=2,
            price_per_night=250.00,
            pet_type=PetType.DOG
        )
        with self.assertRaises(ValidationError):
            room_type.full_clean()

    def test_create_roomtype_invalid_name(self):
        room_type = RoomType(
            hotel=self.hotel,
            name="",
            description="Habitación sin nombre.",
            capacity=2,
            price_per_night=100.00,
            pet_type=PetType.CAT
        )
        with self.assertRaises(ValidationError):
            room_type.full_clean()

    def test_create_roomtype_invalid_description(self):
        room_type = RoomType(
            hotel=self.hotel,
            name="Habitación Económica",
            description="",
            capacity=1,
            price_per_night=50.00,
            pet_type=PetType.ANY
        )
        with self.assertRaises(ValidationError):
            room_type.full_clean()

    def test_create_roomtype_invalid_capacity(self):
        room_type = RoomType(
            hotel=self.hotel,
            name="Habitación Triple",
            description="Habitación espaciosa.",
            capacity=0,
            price_per_night=120.00,
            pet_type=PetType.DOG
        )
        with self.assertRaises(ValidationError):
            room_type.full_clean()

    def test_create_roomtype_invalid_price(self):
        room_type = RoomType(
            hotel=self.hotel,
            name="Habitación VIP",
            description="Habitación con jacuzzi.",
            capacity=2,
            price_per_night=-10.00, 
            pet_type=PetType.CAT
        )
        with self.assertRaises(ValidationError):
            room_type.full_clean()

    def test_create_roomtype_invalid_pet_type(self):
        room_type = RoomType(
            hotel=self.hotel,
            name="Habitación sin mascotas",
            description="No se permiten mascotas.",
            capacity=2,
            price_per_night=90.00,
            pet_type="FISH"  
        )
        with self.assertRaises(ValueError):
            room_type.full_clean()

    