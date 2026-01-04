from rest_framework.test import APITestCase
from django.utils import timezone
from datetime import timedelta
from accounts.models import User
from doctors.models import Doctor
from patients.models import Patient

class AppointmentAPITest(APITestCase):

    def setUp(self):
        self.receptionist = User.objects.create_user(
            username="recept",
            password="pass",
            role="RECEPTIONIST"
        )
        self.client.force_authenticate(user=self.receptionist)

        self.patient = Patient.objects.create(
            first_name="Bob",
            last_name="Marley",
            date_of_birth="1980-01-01",
            gender="M",
            medical_record_number="MRN030"
        )

        doc_user = User.objects.create_user(
            username="doc",
            password="pass",
            role="DOCTOR"
        )

        self.doctor = Doctor.objects.create(
            user=doc_user,
            specialty="ENT",
            license_number="LIC300"
        )

    def test_schedule_appointment(self):
        response = self.client.post("/api/appointments/", {
            "patient": self.patient.id,
            "doctor": self.doctor.id,
            "appointment_datetime": timezone.now() + timedelta(days=2),
            "duration_minutes": 45,
            "reason": "Checkup"
        })

        self.assertEqual(response.status_code, 201)
