from django.urls import path
from .views.health import HealthView
from .views.status import StatusView

urlpatterns = [
    path("health/", HealthView.as_view(), name="health"),
    path("status/", StatusView.as_view(), name="status"),
]
