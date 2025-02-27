from django.test import TestCase
from appUsers.models import AppUser
from django.core.exceptions import ValidationError

class AppUserModelTest(TestCase):

    def test_create_valid_appuser(self):
        user = AppUser.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            phone="+34987654321",
            password="pepitogrillo"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertEqual(user.phone, "+34987654321")

    def test_create_appuser_invalid_email(self):
        user = AppUser.objects.create_user(
            username="invaliduser",
            email="invalid-email",
            phone="+34987654321",
            password="pepitogrillo"
        )
        with self.assertRaises(ValidationError):
            user.full_clean()  

    def test_create_appuser_invalid_phone(self):
        user = AppUser.objects.create_user(
            username="pedro",
            email="validemail@example.com",
            phone="123456789",  
            password="securepassword"
        )
        with self.assertRaises(ValidationError):
            user.full_clean()

    def test_create_appuser_duplicate_email(self):
        AppUser.objects.create_user(
            username="user1",
            email="duplicate@example.com",
            phone="+34987654321",
            password="securepass"
        )
        user = AppUser.objects.create_user(
            username="user2",
            email="duplicate@example.com",
            phone="+34987654322",
            password="securepass12"
        )
        with self.assertRaises(ValidationError):
            user.full_clean()

    def test_create_appuser_blank_email(self):
        user = AppUser.objects.create_user(
            username="juan",
            email="", 
            phone="+34987654321",
            password="juanytolola"
        )
        with self.assertRaises(ValidationError):
            user.full_clean()

    def test_create_appuser_blank_phone(self):
        user = AppUser.objects.create_user(
            username="alberto",
            email="alberto@example.com",
            phone="",  
            password="illojuan"
        )
        with self.assertRaises(ValidationError):
            user.full_clean()