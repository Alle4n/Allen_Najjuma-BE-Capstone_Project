from rest_framework import serializers
from rest_framework.exceptions import APIException
from django.utils import timezone
from datetime import timedelta

from .models import Appointment


class AppointmentConflict(APIException):
    status_code = 409
    default_detail = "Doctor is already booked for this time slot."
    default_code = "appointment_conflict"


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
        read_only_fields = ("id", "created_by", "created_at", "updated_at")

    def validate(self, data):
        """
        Business rules:
        - Cannot schedule appointments in the past
        - Prevent overlapping appointments for the same doctor
        """
        appointment_datetime = data.get(
            "appointment_datetime",
            getattr(self.instance, "appointment_datetime", None),
        )
        duration = data.get(
            "duration_minutes",
            getattr(self.instance, "duration_minutes", None),
        )
        doctor = data.get(
            "doctor",
            getattr(self.instance, "doctor", None),
        )

        if not appointment_datetime or not doctor or not duration:
            return data

        if appointment_datetime < timezone.now():
            raise serializers.ValidationError({
                "appointment_datetime": "Cannot schedule appointment in the past."
            })

        start_time = appointment_datetime
        end_time = start_time + timedelta(minutes=duration)

        qs = Appointment.objects.filter(
            doctor=doctor,
            status="scheduled",
            appointment_datetime__lt=end_time,
        )

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        for existing in qs:
            existing_start = existing.appointment_datetime
            existing_end = existing_start + timedelta(minutes=existing.duration_minutes)

            if existing_start < end_time and existing_end > start_time:
                raise AppointmentConflict()

        return data

    def create(self, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            validated_data["created_by"] = request.user
        return super().create(validated_data)
