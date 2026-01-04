from rest_framework.test import APITestCase
from accounts.models import User

class PatientAPITest(APITestCase):

    def setUp(self):
        self.admin = User.objects.create_user(
            username="admin",
            password="adminpass",
            role="ADMIN"
        )
        self.client.force_authenticate(user=self.admin)

    def test_create_patient(self):
        response = self.client.post("/api/patients/", {
            "first_name": "Alice",
            "last_name": "Smith",
            "date_of_birth": "1992-01-01",
            "gender": "F",
            "medical_record_number": "MRN003"
        })

        self.assertEqual(response.status_code, 201)
