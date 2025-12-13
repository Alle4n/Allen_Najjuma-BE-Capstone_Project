from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from django.http import FileResponse

from .models import Attachment
from .serializers import AttachmentSerializer


class IsDoctorOrNurseOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in ["doctor", "nurse", "admin"]
        )


class AttachmentViewSet(viewsets.ModelViewSet):
    serializer_class = AttachmentSerializer
    permission_classes = [permissions.IsAuthenticated & IsDoctorOrNurseOrAdmin]

    def get_queryset(self):
        """
        Supports:
        /api/attachments/
        /api/patients/{id}/records/{id}/attachments/
        """
        queryset = Attachment.objects.all().select_related(
            "record", "uploaded_by"
        )

        record_id = self.kwargs.get("record_pk")
        if record_id:
            queryset = queryset.filter(record_id=record_id)

        return queryset

    def perform_create(self, serializer):
        record_id = self.kwargs.get("record_pk")

        if record_id:
            serializer.save(
                record_id=record_id,
                uploaded_by=self.request.user
            )
        else:
            serializer.save(uploaded_by=self.request.user)

    @action(detail=True, methods=["get"])
    def download(self, request, pk=None):
        attachment = self.get_object()
        return FileResponse(
            attachment.file.open("rb"),
            as_attachment=True,
            filename=attachment.file.name.split("/")[-1],
        )
