from rest_framework import serializers
from .models import Appointment
from django.utils import timezone
from datetime import timedelta

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
        read_only_fields = ("id", "created_by", "created_at", "updated_at")

    def validate(self, data):
        """
        Validate appointment_datetime not in past and no overlap for doctor.
        """
        appointment_datetime = data.get("appointment_datetime") or getattr(self.instance, "appointment_datetime", None)
        duration = data.get("duration_minutes") or getattr(self.instance, "duration_minutes", 30)
        doctor = data.get("doctor") or getattr(self.instance, "doctor", None)

        if appointment_datetime and appointment_datetime < timezone.now():
            raise serializers.ValidationError("Cannot schedule appointment in the past.")

        # Check overlap: find other appointments for this doctor whose times overlap.
        if doctor and appointment_datetime:
            start = appointment_datetime
            end = appointment_datetime + timedelta(minutes=duration)

            qs = Appointment.objects.filter(doctor=doctor, status="scheduled")
            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)

            # overlap if other.start < end and other.end > start
            for other in qs:
                other_start = other.appointment_datetime
                other_end = other_start + timedelta(minutes=other.duration_minutes)
                if other_start < end and other_end > start:
                    raise serializers.ValidationError(f"Doctor is already booked for {other_start} - {other_end} (appointment id {other.id})")
        return data

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["created_by"] = user
        return super().create(validated_data)
