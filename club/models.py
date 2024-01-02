from django.db import models

# Create your models here.

from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry
from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry

class SportsFacility(models.Model):
    # Fields from the shapefile
    OBJECTID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=48, null=True)
    Type = models.CharField(max_length=32, default='Unknown Type', null=True)
    Address = models.CharField(max_length=78, default='Unknown Address', null=True)
    Telephone = models.CharField(max_length=13, default='Unknown Telephone', null=True)
    Web = models.CharField(max_length=34, null=True, default='Unknown Web')
    Streetview = models.CharField(max_length=78, default='Unknown Streetview', null=True)
    WGS84Longi = models.FloatField(default=0.0, null=True)
    WGS4Latitu = models.FloatField(default=0.0, null=True,)
    Eircode = models.CharField(max_length=7, null=True, default='Unknown Eircode')

    def __str__(self):
        return self.Name

    def __str__(self):
        return self.Name
