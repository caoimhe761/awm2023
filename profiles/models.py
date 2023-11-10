from django.db import models

# Create your models here.
from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=15)

    def __str__(self):
        return str(self.username)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    lon = models.FloatField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    def __str__(self):
        return f"Profile for {self.user.username}"
    # Add other fields as needed

