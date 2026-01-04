from django.contrib import admin
from .models import MedicalRecord

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = (
        "patient",
        "doctor",
        "visit_date",
        "created_at",
    )
    search_fields = (
        "patient__first_name",
        "patient__last_name",
        "doctor__first_name",
        "doctor__last_name",
        "notes",
    )
    list_filter = ("visit_date", "doctor")
    ordering = ("-visit_date",)