from django.contrib import admin
from weather.models.station import Station
from weather.models.reading import Reading

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "latitude", "longitude", "created_at")
    search_fields = ("name", "description")
    list_filter = ("is_active",)
    ordering = ("name",)
    readonly_fields = ("guid", "created_at", "updated_at")

@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ("station", "temperature", "humidity", "wind_dir", "wind_speed",
                    "rain_mm", "luminosity", "measured_at", "created_at")
    search_fields = ("station__name",)
    list_filter = ("station",)
    ordering = ("-created_at",)
    readonly_fields = ("guid", "created_at", "updated_at")
