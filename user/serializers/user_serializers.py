from rest_framework import serializers
from user.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "guid",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "date_joined",
        ]
        read_only_fields = ["guid", "date_joined", "is_staff"]

class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "guid",
            "username",
            "email",
            "first_name",
            "last_name",
        ]
        read_only_fields = ["guid", "username", "email"]
