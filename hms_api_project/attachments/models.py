from django.db import models
from records.models import MedicalRecord

def attachment_upload_path(instance, filename):
    return f"attachments/patient_{instance.record.patient.id}/{filename}"

class Attachment(models.Model):
    record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name="attachments")
    file = models.FileField(upload_to=attachment_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey("accounts.User", on_delete=models.SET_NULL, null=True)
