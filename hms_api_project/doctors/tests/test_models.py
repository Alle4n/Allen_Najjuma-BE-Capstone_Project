from django.test import TestCase
from accounts.models import User
from doctors.models import Doctor

class DoctorModelTest(TestCase):

    def test_create_doctor(self):
        user = User.objects.create_user(
            username="doc",
            password="pass123",
            role="DOCTOR"
        )

        doctor = Doctor.objects.create(
            user=user,
            specialty="Cardiology",
            license_number="LIC001"
        )

        self.assertEqual(doctor.specialty, "Cardiology")
