from django.db import models
from pawtel.roomTypes.models import RoomType


class Room(models.Model):

    is_archived = models.BooleanField(default=False, null=False)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return f"{self.name} ({self.room_type.name})"
