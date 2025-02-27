from rest_framework import serializers
from rooms.models import Room
from roomTypes.models import RoomType 


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            "id", "name", "room_type"
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "name": {"required": True, "max_length": 50},
            "room_type": {"required": True, "allow_null": False},
        }
    