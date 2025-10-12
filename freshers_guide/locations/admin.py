from django.contrib import admin
from .models import Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'block', 'floor', 'contact')
    search_fields = ('name', 'type')
