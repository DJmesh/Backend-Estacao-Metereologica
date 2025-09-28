from django.urls import path, include
from rest_framework.routers import DefaultRouter
from weather.views.station_views import StationViewSet
from weather.views.reading_views import ReadingViewSet

router = DefaultRouter()
router.register(r'stations', StationViewSet, basename='station')
router.register(r'readings', ReadingViewSet, basename='reading')

urlpatterns = [
    path('', include(router.urls)),
]
