from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import uuid

class Patient(models.Model):
    GENDER_CHOICES = (("male","Male"), ("female","Female"), ("other","Other"))
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    contact_phone = models.CharField(max_length=30, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    emergency_contact = models.CharField(max_length=255, blank=True, null=True)
    medical_record_number = models.CharField(max_length=64, unique=True, default=uuid.uuid4)
    created_at = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.medical_record_number})"
