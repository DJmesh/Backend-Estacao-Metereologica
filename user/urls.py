from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.views.user_views import UserViewSet, MeView
from user.views.register import RegisterView
from user.views.password_reset import PasswordResetRequestView, PasswordResetConfirmView

router = DefaultRouter()
router.register(r"", UserViewSet, basename="user")

urlpatterns = [
    path("register/", RegisterView.as_view(), name="user-register"),
    path("password/reset/", PasswordResetRequestView.as_view(), name="password-reset"),
    path("password/reset/confirm/", PasswordResetConfirmView.as_view(), name="password-reset-confirm"),

    path("me/", MeView.as_view(), name="user-me"),

    path("", include(router.urls)),
]
