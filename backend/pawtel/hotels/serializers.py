from rest_framework import serializers
from hotels.models import Hotel
from hotelOwners.models import HotelOwner

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = [
            "id", "name", "address", "city", "description", "hotel_owner"
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "name": {"required": True, "max_length": 100},
            "address": {"required": True, "max_length": 100},
            "city": {"required": True, "max_length": 50},
            "description": {"required": True, "max_length": 300},
            "hotel_owner": {"required": True, "allow_null": False},
        }
