from django.urls import path

from expense_tracker.tracker.views import RecordDetailView
from expense_tracker.tracker.views import RecordListView

app_name = "tracker"
urlpatterns = [
    path("record/", view=RecordListView.as_view(), name="record-list"),
    path("record/<int:pk>/", view=RecordDetailView.as_view(), name="record-detail"),
]
