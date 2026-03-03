from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from expense_tracker.tracker.api.views import RecordDetailView
from expense_tracker.tracker.api.views import RecordView
from expense_tracker.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls
urlpatterns += [
    path("record/", view=RecordView.as_view(), name="record-list"),
    path(
        "record/<int:pk>/",
        view=RecordDetailView.as_view(),
        name="record-detail",
    ),
]
