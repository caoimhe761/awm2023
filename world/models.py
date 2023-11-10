
# Create your models here.
from django.contrib.gis.db import models
import geocoder

from django.contrib.gis.db import models

class WorldBorder(models.Model):
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2, null=True)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    class Meta:
        verbose_name_plural = 'WorldBorder'
        
    def save(self, *args, **kwargs):
        self.lat = geocoder.osm(self.name).lat
        self.lon= geocoder.osm(self.name).lng
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
