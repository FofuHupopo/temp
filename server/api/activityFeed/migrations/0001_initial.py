# Generated by Django 4.0.6 on 2023-05-17 11:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='news/files/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
                'db_table': 'news_file',
            },
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news/images/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
                'db_table': 'news_image',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('body', models.TextField(verbose_name='Содержимое')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('styles', models.JSONField(blank=True, default=dict, verbose_name='Стили')),
                ('is_important', models.BooleanField(default=False, verbose_name='Важное сообщение')),
                ('category', models.CharField(choices=[('for_all', 'Для всех'), ('for_managers', 'Для менеджеров'), ('for_drivers', 'Для водителей'), ('for_clients', 'Для клиентов')], default='for_all', max_length=16, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'db_table': 'news',
            },
        ),
    ]
