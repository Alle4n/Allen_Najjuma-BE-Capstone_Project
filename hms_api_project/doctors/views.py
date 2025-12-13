from rest_framework import viewsets, permissions, filters
from .models import Doctor
from .serializers import DoctorSerializer

class IsAdminOrSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role == "admin":
            return True
        # doctor may edit their profile
        if hasattr(request.user, "doctor_profile"):
            return obj.user_id == request.user.id
        return False

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by("last_name")
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["first_name", "last_name", "specialty"]
