from django.db import models
from django.conf import settings

class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="doctor_profile", null=True, blank=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    specialty = models.CharField(max_length=120)
    license_number = models.CharField(max_length=64, unique=True)
    contact_phone = models.CharField(max_length=30, blank=True, null=True)
    available_hours = models.JSONField(default=dict, blank=True)  # e.g. {"mon": ["09:00-12:00", "14:00-17:00"], ...}
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.specialty}"
