# Generated by Django 4.0.6 on 2022-09-29 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tariffs', '0007_remove_tariff_companies_tariff_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariff',
            name='title',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='type',
            field=models.CharField(choices=[('basic', 'Основной'), ('commission', 'Комиссионный'), ('company', 'Для компании')], default='Основной', max_length=32, verbose_name='Тип'),
        ),
    ]