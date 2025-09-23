from rest_framework import serializers
from weather.models.reading import Reading

class ReadingSerializer(serializers.ModelSerializer):
    station_name = serializers.ReadOnlyField(source="station.name")

    class Meta:
        model = Reading
        fields = [
            "guid",
            "station",
            "station_name",
            "humidity",
            "temperature",
            "wind_dir",
            "wind_speed",
            "rain_mm",
            "luminosity",
            "measured_at",
            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):
        hum = attrs.get("humidity", None)
        wd = attrs.get("wind_dir", None)
        if hum is not None and not (0.0 <= hum <= 100.0):
            raise serializers.ValidationError({"humidity": "Deve estar entre 0 e 100."})
        if wd is not None and not (0.0 <= wd < 360.0):
            raise serializers.ValidationError({"wind_dir": "Deve estar entre 0 e 359.99."})
        return attrs
