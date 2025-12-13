from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="medical_records")
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name="medical_records")
    visit_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()
    diagnosis_codes = models.JSONField(default=list, blank=True)  # store list of ICD-10 codes
    prescriptions = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
