from django.db import models
import geocoder


class Location(models.Model):
    place_name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.place_name).lat
        self.longitude = geocoder.osm(self.place_name).lng
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.place_name

class HockeyClub(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

class Fixture(models.Model):
    team_name1 = models.CharField(max_length=255)
    team_name2 = models.CharField(max_length=255)
    date = models.DateField()
    time = models.CharField(max_length=10)
    venue = models.CharField(max_length=255)
    league = models.CharField(max_length=255)
