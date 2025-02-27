from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class AppUser(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+34\d{9}$',
        message="Phone number must be in the format: +34XXXXXXXXX"
    )
    
    phone = models.CharField(validators=[phone_regex], max_length=13, unique=True, blank=False)
    email = models.EmailField(unique=True, blank=False, max_length=100)

    def __str__(self):
        return f"{self.username}"