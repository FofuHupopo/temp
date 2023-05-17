# Generated by Django 4.0.6 on 2022-10-15 11:08

import api.tariffs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tariffs', '0018_remove_intracitytariff_city_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intracitytariff',
            name='prices',
            field=models.ManyToManyField(default=api.tariffs.models.set_default_car_classes_price, to='tariffs.pricetocarclass', verbose_name='Цены к классу авто'),
        ),
    ]