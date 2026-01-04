from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "patient",
        "doctor",
        "appointment_datetime",
        "duration_minutes",
        "status",
        "created_by",
        "created_at",
    )
    list_filter = ("status", "doctor", "appointment_datetime")
    search_fields = (
        "patient__first_name",
        "patient__last_name",
        "doctor__first_name",
        "doctor__last_name",
    )
    ordering = ("appointment_datetime",)