from django.contrib import admin
from django.http import HttpResponse
import csv
from weather.models import Station, Reading

class ReadingInline(admin.TabularInline):
    model = Reading
    extra = 0
    fields = ("measured_at", "temperature", "humidity", "wind_dir", "wind_speed", "rain_mm", "luminosity", "created_at")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "latitude", "longitude", "created_at")
    list_filter = ("is_active",)
    search_fields = ("name", "description")
    date_hierarchy = "created_at"
    ordering = ("name",)
    inlines = [ReadingInline]
    save_on_top = True

@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ("station", "measured_at", "temperature", "humidity", "wind_dir", "wind_speed", "rain_mm", "created_at")
    list_filter = ("station", "measured_at")
    search_fields = ("station__name",)
    date_hierarchy = "created_at"
    readonly_fields = ("created_at", "updated_at")
    autocomplete_fields = ("station",)
    ordering = ("-created_at",)
    save_on_top = True
    actions = ["export_as_csv"]

    @admin.action(description="Exportar CSV (selecionados)")
    def export_as_csv(self, request, queryset):
        fields = ["guid","station_id","measured_at","temperature","humidity","wind_dir","wind_speed","rain_mm","luminosity","created_at"]
        resp = HttpResponse(content_type="text/csv")
        resp["Content-Disposition"] = "attachment; filename=readings.csv"
        writer = csv.writer(resp)
        writer.writerow(fields)
        for obj in queryset.only(*[f.split("_id")[0] if f.endswith("_id") else f for f in fields]):
            row = [
                obj.guid, getattr(obj, "station_id"), obj.measured_at, obj.temperature, obj.humidity,
                obj.wind_dir, obj.wind_speed, obj.rain_mm, obj.luminosity, obj.created_at
            ]
            writer.writerow(row)
        return resp
