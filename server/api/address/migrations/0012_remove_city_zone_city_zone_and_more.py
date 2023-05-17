# Generated by Django 4.0.6 on 2022-10-14 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0008_alter_globaladdress_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='zone',
            field=models.ManyToManyField(blank=True, related_name='zone', to='address.coordinate', verbose_name='координаты'),
        ),
    ]
