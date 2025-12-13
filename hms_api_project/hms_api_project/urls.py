from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_nested.routers import NestedDefaultRouter

from accounts.views import UserViewSet
from patients.views import PatientViewSet
from doctors.views import DoctorViewSet
from appointments.views import AppointmentViewSet
from records.views import MedicalRecordViewSet
from attachments.views import AttachmentViewSet


# -------------------------
# Base Router
# -------------------------
router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")
router.register(r"patients", PatientViewSet, basename="patients")
router.register(r"doctors", DoctorViewSet, basename="doctors")
router.register(r"appointments", AppointmentViewSet, basename="appointments")
router.register(r"records", MedicalRecordViewSet, basename="records")


# -------------------------
# Nested Router Level 1
# /patients/{patient_id}/records/
# -------------------------
patients_router = NestedDefaultRouter(router, r"patients", lookup="patient")
patients_router.register(
    r"records",
    MedicalRecordViewSet,
    basename="patient-records"
)

# -------------------------
# Nested Router Level 2
# /patients/{patient_id}/records/{record_id}/attachments/
# -------------------------
records_router = NestedDefaultRouter(patients_router, r"records", lookup="record")
records_router.register(
    r"attachments",
    AttachmentViewSet,
    basename="record-attachments"
)


def home(request):
    return JsonResponse({
        "message": "HMS API is running",
        "endpoints": {
            "auth_token": "/api/auth/token/",
            "refresh_token": "/api/auth/token/refresh/",
            "users": "/api/users/",
            "patients": "/api/patients/",
            "patient_records": "/api/patients/{id}/records/",
            "record_attachments": "/api/patients/{patient_id}/records/{record_id}/attachments/",
        }
    })


# -------------------------
# URL Patterns
# -------------------------
urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),

    # Auth
    path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # API Routes
    path("api/", include(router.urls)),
    path("api/", include(patients_router.urls)),
    path("api/", include(records_router.urls)),
]
