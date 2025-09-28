from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from user.views.auth_views import JwtTokenObtainPairView, JwtTokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Auth (tag "Auth")
    path('api/auth/token/', JwtTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', JwtTokenRefreshView.as_view(), name='token_refresh'),

    # Core e Weather
    path('api/core/', include('core.urls')),
    path('', include('weather.urls')),
]
