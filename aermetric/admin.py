from django.contrib import admin

from aermetric.models import AircraftErrorData


class AircraftErrorDataAdmin(admin.ModelAdmin):
    list_display = ["id", "priority", "type", "aircraft", "status", "errors_count", "info_count"]


admin.site.register(AircraftErrorData, AircraftErrorDataAdmin)
