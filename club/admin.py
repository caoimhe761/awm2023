from django.contrib import admin

# Register your models here.

from django.contrib.gis import admin
from .models import SportsFacility

class DataAdmin(admin.ModelAdmin):
    list_display = ('OBJECTID','Name','Type','Address','Telephone','Web','Streetview','WGS84Longi','WGS4Latitu','Eircode')
admin.site.register(SportsFacility, admin.ModelAdmin)
