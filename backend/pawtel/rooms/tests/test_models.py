from django.test import TestCase
from rooms.models import Room
from roomTypes.models import RoomType
from hotels.models import Hotel
from hotelOwners.models import HotelOwner
from django.core.exceptions import ValidationError

class RoomModelTest(TestCase):

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

        self.room_type = RoomType.objects.create(
            hotel=self.hotel,
            name="Suite Deluxe",
            description="Una habitación lujosa con vista al mar.",
            capacity=2,
            price_per_night=150.00,
            pet_type="DOG"
        )

    def test_create_valid_room(self):
        room = Room.objects.create(
            name="Habitación 101",
            room_type=self.room_type
        )
        self.assertEqual(room.name, "Habitación 101")
        self.assertEqual(room.room_type, self.room_type)
        self.assertEqual(room.room_type.hotel, self.hotel)  
        self.assertEqual(room.room_type.hotel.hotel_owner, self.owner)  

    
    def test_create_room_invalid_name(self):
    
        room = Room(
            name="",  
            room_type=self.room_type
        )
        with self.assertRaises(ValidationError):
            room.full_clean()

    
    def test_create_room_invalid_room_type(self):
        room = Room(
            name="Habitación sin Tipo",
            room_type=None  
        )
        with self.assertRaises(ValidationError):
            room.full_clean()