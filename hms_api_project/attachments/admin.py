from django.contrib import admin
from .models import Attachment

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = (
        "record",
        "file",
        "uploaded_by",
        "uploaded_at",
    )
    search_fields = (
        "record__patient__first_name",
        "record__patient__last_name",
        "record__doctor__first_name",
        "record__doctor__last_name",
        "file",
    )
    list_filter = ("uploaded_at", "uploaded_by")
    ordering = ("-uploaded_at",)
