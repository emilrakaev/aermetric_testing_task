# Generated by Django 4.0.4 on 2022-05-30 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aermetric', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AircraftErrorData',
            new_name='AircraftStatData',
        ),
    ]