# Generated by Django 4.0.6 on 2022-10-08 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0007_remove_coordinate_unique_coords_and_more'),
        ('tariffs', '0010_citytoprice_converse'),
    ]

    operations = [
        migrations.CreateModel(
            name='HubToPriceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField(default=-1, verbose_name='Расстояние')),
                ('hours_duration', models.IntegerField(default=-1, verbose_name='Часы')),
                ('minutes_duration', models.IntegerField(default=-1, verbose_name='Минуты')),
                ('hubs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.hub', verbose_name='В хаб')),
                ('prices', models.ManyToManyField(blank=True, to='tariffs.pricetocarclass')),
            ],
            options={
                'verbose_name': 'Хаб к ценам',
                'verbose_name_plural': 'Хабы к ценам',
                'db_table': 'hub_to_price_intercity',
            },
        ),
        migrations.AddField(
            model_name='intercitytariff',
            name='hubs',
            field=models.ManyToManyField(blank=True, to='tariffs.hubtopricemodel', verbose_name='В хабы'),
        ),
    ]