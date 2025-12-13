from rest_framework import viewsets, permissions, filters
from .models import Patient
from .serializers import PatientSerializer
from django_filters.rest_framework import DjangoFilterBackend

class IsStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.filter(is_deleted=False).order_by("-created_at")
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["gender", "medical_record_number"]
    search_fields = ["first_name", "last_name", "medical_record_number"]
    ordering_fields = ["created_at", "last_name"]
