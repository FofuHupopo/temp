# Generated by Django 4.0.6 on 2022-10-08 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0007_remove_coordinate_unique_coords_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globaladdress',
            name='address',
            field=models.CharField(max_length=256, unique=True, verbose_name='адрес'),
        ),
    ]