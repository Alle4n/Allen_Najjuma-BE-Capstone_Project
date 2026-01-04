from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from appointments.models import Appointment
from accounts.models import User
from doctors.models import Doctor
from patients.models import Patient

class AppointmentOverlapTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username="doc",
            password="pass",
            role="DOCTOR"
        )

        self.doctor = Doctor.objects.create(
            user=user,
            specialty="General",
            license_number="LIC200"
        )

        self.patient = Patient.objects.create(
            first_name="Anna",
            last_name="Lee",
            date_of_birth="1995-01-01",
            gender="F",
            medical_record_number="MRN020"
        )

    def test_overlapping_appointments_not_allowed(self):
        start = timezone.now() + timedelta(days=1)

        Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            appointment_datetime=start,
            duration_minutes=60,
            status="scheduled"
        )

        appt = Appointment(
            patient=self.patient,
            doctor=self.doctor,
            appointment_datetime=start + timedelta(minutes=30),
            duration_minutes=30,
            status="scheduled"
        )

        with self.assertRaises(ValueError):
            appt.full_clean()
