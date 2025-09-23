from django.db import models
from base.models.base import BaseModel
from weather.models.station import Station

class Reading(BaseModel):
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="readings")

    humidity = models.FloatField(null=True, blank=True)     # %
    temperature = models.FloatField(null=True, blank=True)  # °C
    wind_dir = models.FloatField(null=True, blank=True)     # 0-360 graus
    wind_speed = models.FloatField(null=True, blank=True)   # m/s ou km/h
    rain_mm = models.FloatField(null=True, blank=True)      # mm no período
    luminosity = models.FloatField(null=True, blank=True)   # lux

    measured_at = models.DateTimeField(null=True, blank=True, help_text="Momento da medição (opcional)")

    class Meta:
        verbose_name = "Leitura"
        verbose_name_plural = "Leituras"
        indexes = [
            models.Index(fields=["station", "created_at"]),
            models.Index(fields=["measured_at"]),
        ]

    def __str__(self):
        return f"{self.station.name} @ {self.created_at:%Y-%m-%d %H:%M:%S}"
