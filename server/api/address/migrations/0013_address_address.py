# Generated by Django 4.0.6 on 2022-10-16 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0012_remove_city_zone_city_zone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='address',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Сырые данные'),
        ),
    ]
