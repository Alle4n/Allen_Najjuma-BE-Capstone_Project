from rest_framework.test import APITestCase
from accounts.models import User

class DoctorPermissionTest(APITestCase):

    def setUp(self):
        self.doctor = User.objects.create_user(
            username="doc",
            password="pass",
            role="DOCTOR"
        )
        self.client.force_authenticate(user=self.doctor)

    def test_doctor_cannot_create_doctor_profile(self):
        response = self.client.post("/api/doctors/", {
            "specialty": "Neurology",
            "license_number": "LIC999"
        })

        self.assertEqual(response.status_code, 403)
