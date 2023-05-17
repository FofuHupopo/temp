# Generated by Django 4.0.6 on 2022-09-29 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_bankmodel_rename_user_company_owner_and_more'),
        ('tariffs', '0006_remove_tariff_is_commission_alter_tariff_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tariff',
            name='companies',
        ),
        migrations.AddField(
            model_name='tariff',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profile.company', verbose_name='Компания'),
        ),
    ]