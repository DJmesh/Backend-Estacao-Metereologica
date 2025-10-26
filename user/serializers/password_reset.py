from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import serializers

User = get_user_model()
token_generator = PasswordResetTokenGenerator()


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        return value.strip().lower()

    def create(self, validated_data):
        user = User.objects.filter(email__iexact=validated_data["email"]).first()
        if not user:
            return {"sent": True}

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user)

        payload = {"sent": True}
        if getattr(settings, "DEBUG", False):
            payload.update({"uid": uid, "token": token})
        return payload


class PasswordResetConfirmSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True, trim_whitespace=False)
    new_password_confirm = serializers.CharField(write_only=True, trim_whitespace=False)

    def validate(self, attrs):
        if attrs["new_password"] != attrs["new_password_confirm"]:
            raise serializers.ValidationError({"new_password_confirm": "Passwords do not match."})
        return attrs

    def save(self, **kwargs):
        try:
            user_id = force_str(urlsafe_base64_decode(self.validated_data["uid"]))
            user = User.objects.get(pk=user_id)
        except Exception:
            raise serializers.ValidationError({"uid": "Invalid uid."})

        if not token_generator.check_token(user, self.validated_data["token"]):
            raise serializers.ValidationError({"token": "Invalid or expired token."})

        user.set_password(self.validated_data["new_password"])
        user.save(update_fields=["password"])
        return {"reset": True}
