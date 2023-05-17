# Generated by Django 4.0.6 on 2023-05-17 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activityFeed', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор'),
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='news',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='activityFeed.news'),
        ),
        migrations.AddField(
            model_name='filemodel',
            name='news',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='activityFeed.news'),
        ),
    ]
