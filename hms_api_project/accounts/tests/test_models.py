from django.test import TestCase
from accounts.models import User

class UserModelTest(TestCase):

    def test_create_user_with_role(self):
        user = User.objects.create_user(
            username="doctor1",
            password="testpass123",
            role="DOCTOR"
        )

        self.assertEqual(user.username, "doctor1")
        self.assertEqual(user.role, "DOCTOR")
        self.assertTrue(user.check_password("testpass123"))
