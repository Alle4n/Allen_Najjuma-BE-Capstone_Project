from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("doctor", "Doctor"),
        ("nurse", "Nurse"),
        ("receptionist", "Receptionist"),
        ("billing", "Billing"),
    )
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default="receptionist")

    def is_admin(self):
        return self.role == "admin"