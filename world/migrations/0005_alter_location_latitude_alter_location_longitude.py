# Generated by Django 4.2.7 on 2023-11-14 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0004_location_delete_worldborder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.FloatField(default=0),
        ),
    ]
