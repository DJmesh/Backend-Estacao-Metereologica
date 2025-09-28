from django.db import models
from base.models import BaseModel

class Station(BaseModel):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True, default="")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Estação"
        verbose_name_plural = "Estações"

    def __str__(self) -> str:
        return self.name
