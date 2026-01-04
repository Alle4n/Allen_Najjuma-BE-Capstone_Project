from rest_framework import serializers
from .models import Patient
from django.utils import timezone

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            "id",
            "first_name",
            "last_name",
            "date_of_birth",
            "gender",
            "contact_phone",
            "contact_email",
            "address",
            "emergency_contact",
            "medical_record_number",
            "created_at",
            "is_deleted",
        ]
        read_only_fields = ("id", "created_at", "is_deleted", "medical_record_number")

    # Validate first_name
    def validate_first_name(self, value):
        if not value:
            raise serializers.ValidationError("First name is required.")
        return value

    # Validate last_name
    def validate_last_name(self, value):
        if not value:
            raise serializers.ValidationError("Last name is required.")
        return value

    # Validate date_of_birth
    def validate_date_of_birth(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Date of birth cannot be in the future.")
        return value

    # Optional: restrict access to deleted patients
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        user = self.context.get("request").user if self.context.get("request") else None

        # Example: hide contact info for unauthorized users
        if user and user.role not in ["ADMIN", "DOCTOR", "NURSE"]:
            rep.pop("contact_phone", None)
            rep.pop("contact_email", None)
            rep.pop("emergency_contact", None)

        return rep
