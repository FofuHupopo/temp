# Generated by Django 4.0.6 on 2022-10-07 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0006_hubzone_title'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='coordinate',
            name='unique_coords',
        ),
        migrations.RemoveField(
            model_name='globaladdress',
            name='city',
        ),
    ]
