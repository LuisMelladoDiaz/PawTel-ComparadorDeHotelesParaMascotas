from django.test import TestCase
from hotelOwners.models import HotelOwner

class HotelOwnerModelTest(TestCase):

    def test_create_valid_hotel_owner(self):
        owner = HotelOwner.objects.create_user(
            username="hotelowner2",
            first_name="Johny",
            last_name="Does",
            email="owne@example.com",
            phone="+34987654324",
            password="securepasswo"
        )

        # Verification data stored correctly
        self.assertEqual(owner.username, "hotelowner2")
        self.assertEqual(owner.first_name, "Johny")
        self.assertEqual(owner.last_name, "Does")
        self.assertEqual(owner.email, "owne@example.com")
        self.assertEqual(owner.phone, "+34987654324")
        self.assertTrue(owner.check_password("securepasswo"))  

        # Verify that it has corrrect permissions
        self.assertTrue(owner.is_active) 
        self.assertFalse(owner.is_staff) 
        self.assertFalse(owner.is_superuser)  