from django.urls import path

from expense_tracker.tracker.views import RecordCreateView
from expense_tracker.tracker.views import RecordDetailView
from expense_tracker.tracker.views import RecordListView
from expense_tracker.tracker.views import RecordUpdateView

app_name = "tracker"
urlpatterns = [
    path("record/", view=RecordListView.as_view(), name="record-list"),
    path("record/add/", view=RecordCreateView.as_view(), name="record-create"),
    path("record/<int:pk>/", view=RecordDetailView.as_view(), name="record-detail"),
    path("record/<int:pk>/edit/", view=RecordUpdateView.as_view(), name="record-edit"),
]
