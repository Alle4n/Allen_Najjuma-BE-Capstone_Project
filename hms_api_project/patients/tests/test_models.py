from django.test import TestCase
from patients.models import Patient
from datetime import date

class PatientModelTest(TestCase):

    def test_create_patient(self):
        patient = Patient.objects.create(
            first_name="John",
            last_name="Doe",
            date_of_birth=date(1990, 1, 1),
            gender="M",
            medical_record_number="MRN001"
        )

        self.assertEqual(patient.first_name, "John")
        self.assertEqual(patient.medical_record_number, "MRN001")

    def test_unique_medical_record_number(self):
        Patient.objects.create(
            first_name="Jane",
            last_name="Doe",
            date_of_birth=date(1985, 1, 1),
            gender="F",
            medical_record_number="MRN002"
        )

        with self.assertRaises(Exception):
            Patient.objects.create(
                first_name="Jim",
                last_name="Beam",
                date_of_birth=date(1980, 1, 1),
                gender="M",
                medical_record_number="MRN002"
            )
