from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "medical_record_number",
        "gender",
        "date_of_birth",
        "contact_phone",
        "created_at",
        "is_deleted",
    )
    list_filter = ("gender", "is_deleted", "created_at")
    search_fields = (
        "first_name",
        "last_name",
        "medical_record_number",
        "contact_phone",
        "contact_email",
    )
    ordering = ("-created_at",)
