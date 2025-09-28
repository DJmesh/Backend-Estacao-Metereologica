from rest_framework import serializers
from weather.models.station import Station

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ["guid", "name", "description", "latitude", "longitude", "is_active", "created_at", "updated_at"]
