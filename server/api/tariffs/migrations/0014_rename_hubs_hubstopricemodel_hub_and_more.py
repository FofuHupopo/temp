# Generated by Django 4.0.6 on 2022-10-08 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tariffs', '0013_rename_hubs_intercitytariff_hub'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hubstopricemodel',
            old_name='hubs',
            new_name='hub',
        ),
        migrations.RenameField(
            model_name='intercitytariff',
            old_name='hub',
            new_name='hubs',
        ),
    ]