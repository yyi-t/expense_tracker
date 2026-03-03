from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from expense_tracker.tracker.api.serializers import RecordCreateSerializer
from expense_tracker.tracker.api.serializers import RecordSerializer
from expense_tracker.tracker.api.serializers import RecordUpdateSerializer
from expense_tracker.tracker.models import Record


class RecordView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return RecordCreateSerializer
        return RecordSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Record.objects.filter(user=self.request.user)
        return []

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in {"PUT", "PATCH"}:
            return RecordUpdateSerializer
        return RecordSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Record.objects.filter(user=self.request.user)
        return []
