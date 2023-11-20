from django.contrib.gis.db import models
import geocoder

class Location(models.Model):
    place_name = models.CharField(max_length=255)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.place_name).lat
        self.longitude = geocoder.osm(self.place_name).lng
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.place_name