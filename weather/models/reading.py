from django.db import models
from base.models import BaseModel
from weather.models.station import Station

class Reading(BaseModel):
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="readings")

    humidity = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    wind_dir = models.FloatField(null=True, blank=True)   # degrees 0..360
    wind_speed = models.FloatField(null=True, blank=True) # m/s or km/h
    rain_mm = models.FloatField(null=True, blank=True)    # mm in period
    luminosity = models.FloatField(null=True, blank=True) # lux

    measured_at = models.DateTimeField(null=True, blank=True, help_text="Optional reading datetime.")

    class Meta:
        verbose_name = "Leitura"
        verbose_name_plural = "Leituras"
        indexes = [
            models.Index(fields=["station", "created_at"]),
            models.Index(fields=["measured_at"]),
        ]

    def __str__(self) -> str:
        return f"{self.station.name} @ {self.created_at:%Y-%m-%d %H:%M:%S}"
