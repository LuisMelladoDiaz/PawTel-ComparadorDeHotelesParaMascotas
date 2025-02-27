from rest_framework import serializers
from roomTypes.models import RoomType
from hotels.models import Hotel

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = [
            "id", "name", "description", "capacity", "price_per_night", "pet_type", "hotel"
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "name": {"required": True, "max_length": 50},
            "description": {"required": True, "max_length": 300},
            "capacity": {"required": True, "min_value": 1, "allow_null": False},
            "price_per_night": {"required": True, "min_value": 1.00, "max_digits": 6, "decimal_places": 2, "allow_null": False},
            "pet_type": {"required": True, "allow_null": False},
            "hotel": {"required": True, "allow_null": False},
        }
