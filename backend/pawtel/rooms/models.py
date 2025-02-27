from django.db import models
from roomTypes.models import RoomType  

class Room(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f"{self.name} ({self.room_type.name})"