# Generated by Django 4.0.6 on 2022-09-19 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('bic', models.CharField(max_length=9, verbose_name='БИК')),
            ],
            options={
                'verbose_name': 'Банк',
                'verbose_name_plural': 'Банки',
                'db_table': 'bank',
            },
        ),
        migrations.RenameField(
            model_name='company',
            old_name='user',
            new_name='owner',
        ),
        migrations.RemoveField(
            model_name='company',
            name='financial_turnover',
        ),
        migrations.RemoveField(
            model_name='company',
            name='gen_director_name',
        ),
        migrations.RemoveField(
            model_name='company',
            name='gen_director_patronymic',
        ),
        migrations.RemoveField(
            model_name='company',
            name='gen_director_surname',
        ),
        migrations.RemoveField(
            model_name='company',
            name='status',
        ),
        migrations.AddField(
            model_name='company',
            name='checking_account',
            field=models.CharField(default='', max_length=20, verbose_name='Расчетный счет'),
        ),
        migrations.AddField(
            model_name='company',
            name='corporate_account',
            field=models.CharField(default='', max_length=20, verbose_name='Корпоративный счет'),
        ),
        migrations.AddField(
            model_name='company',
            name='rrc',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='КПП'),
        ),
        migrations.AddField(
            model_name='company',
            name='tin',
            field=models.CharField(default='', max_length=12, verbose_name='ИНН'),
        ),
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'db_table': 'employee',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='bank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='profile.bankmodel', verbose_name='Банк'),
        ),
        migrations.AddField(
            model_name='company',
            name='employees',
            field=models.ManyToManyField(blank=True, to='profile.employeemodel'),
        ),
    ]
