from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from weather.views.station_views import StationViewSet
from weather.views.reading_views import ReadingViewSet
from user.views.user_views import UserViewSet, MeView
from core.views.health import HealthView

router = DefaultRouter()
router.register(r"stations", StationViewSet, basename="station")
router.register(r"readings", ReadingViewSet, basename="reading")
router.register(r"users", UserViewSet, basename="user")  # admin/gestão de usuários

urlpatterns = [
    path("admin/", admin.site.urls),

    # Auth JWT
    path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Health (público)
    path("api/health/", HealthView.as_view(), name="health"),

    # Perfil do usuário logado
    path("api/me/", MeView.as_view(), name="me"),

    # API principal
    path("api/", include(router.urls)),

    # OpenAPI
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    # Swagger protegido por JWT
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema", permission_classes=[IsAuthenticated]),
        name="swagger-ui",
    ),
]
