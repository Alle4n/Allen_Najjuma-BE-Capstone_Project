from rest_framework import viewsets, permissions, filters
from .models import Appointment
from .serializers import AppointmentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by("-appointment_datetime")
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["doctor", "patient", "status"]
    search_fields = ["reason"]

    @action(detail=False, methods=["get"])
    def upcoming(self, request):
        from django.utils import timezone
        qs = self.get_queryset().filter(appointment_datetime__gte=timezone.now(), status="scheduled")
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
