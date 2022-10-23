# Generated by Django 3.2.7 on 2021-09-25 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(verbose_name='Начало вахты')),
                ('date_end', models.DateField(verbose_name='Конец вахты')),
                ('days_road', models.IntegerField(verbose_name='Дни в пути')),
                ('hourly_fee', models.FloatField(verbose_name='Оплата в час')),
                ('district_coefficient', models.IntegerField(verbose_name='Районный коэффициент')),
                ('northern_coefficient', models.IntegerField(verbose_name='Северный коэффициент')),
                ('award', models.IntegerField(verbose_name='Премия')),
                ('extras', models.IntegerField(verbose_name='Доплата')),
                ('holiday', models.IntegerField(verbose_name='Количество праздников')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
