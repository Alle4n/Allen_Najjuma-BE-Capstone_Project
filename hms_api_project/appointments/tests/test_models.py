from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from appointments.models import Appointment
from accounts.models import User
from doctors.models import Doctor
from patients.models import Patient

class AppointmentModelTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username="doc",
            password="pass",
            role="DOCTOR"
        )
        self.doctor = Doctor.objects.create(
            user=user,
            specialty="General",
            license_number="LIC100"
        )

        self.patient = Patient.objects.create(
            first_name="Tom",
            last_name="Hardy",
            date_of_birth="1990-01-01",
            gender="M",
            medical_record_number="MRN010"
        )

    def test_create_appointment(self):
        appt = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            appointment_datetime=timezone.now() + timedelta(days=1),
            duration_minutes=30,
            status="scheduled"
        )

        self.assertEqual(appt.status, "scheduled")
