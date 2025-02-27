from rest_framework import serializers 
from appUsers.models import AppUser  

class AppUserSerializer(serializers.ModelSerializer):  
    class Meta:
        model = AppUser  
        fields = [  
            "id", "username", "first_name", "last_name", "email", "phone",
            "date_joined", "last_login", "is_active", "is_staff", "is_superuser"
        ]
        
        extra_kwargs = {  
            "id": {"read_only": True},
            "password": {"write_only": True},
            "email": {"required": True, "max_length": 100},  
            "phone": {"required": True, "max_length": 13, "validators": [AppUser.phone_regex], "allow_null": False},
        }

