# Generated by Django 4.2.7 on 2023-11-10 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_remove_profile_location_profile_lat_profile_lon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]