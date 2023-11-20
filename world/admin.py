
from django.contrib.gis import admin
from .models import Location

class DataAdmin(admin.ModelAdmin):
    list_display = ('place_name','latitude', 'longitude')
admin.site.register(Location, admin.ModelAdmin)

