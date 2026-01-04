from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "specialty",
        "license_number",
        "contact_phone",
        "created_at",
    )
    search_fields = (
        "first_name",
        "last_name",
        "specialty",
        "license_number",
        "contact_phone",
    )
    ordering = ("last_name", "first_name")