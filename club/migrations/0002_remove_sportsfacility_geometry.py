# Generated by Django 4.2.8 on 2023-12-30 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sportsfacility',
            name='geometry',
        ),
    ]