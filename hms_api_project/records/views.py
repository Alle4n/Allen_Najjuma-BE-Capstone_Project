from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import MedicalRecord
from .serializers import MedicalRecordSerializer


class IsDoctorOrNurseOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in ["doctor", "nurse", "admin"]
        )


class MedicalRecordViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalRecordSerializer
    permission_classes = [permissions.IsAuthenticated & IsDoctorOrNurseOrAdmin]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["patient", "doctor"]
    search_fields = ["notes"]

    def get_queryset(self):
        """
        Supports:
        - /api/records/
        - /api/patients/{id}/records/
        """
        queryset = MedicalRecord.objects.all().order_by("-visit_date")

        # Nested route support
        patient_id = self.kwargs.get("patient_pk")
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)

        return queryset

    def perform_create(self, serializer):
        """
        Automatically associate patient when creating via:
        POST /api/patients/{id}/records/
        """
        patient_id = self.kwargs.get("patient_pk")
        if patient_id:
            serializer.save(patient_id=patient_id)
        else:
            serializer.save()
