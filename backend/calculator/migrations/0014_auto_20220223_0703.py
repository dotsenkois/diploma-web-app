# Generated by Django 3.2.7 on 2022-02-23 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0013_alter_profile_hourly_fee'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='holidays',
            options={'verbose_name': 'Праздник', 'verbose_name_plural': 'Праздники'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Запись', 'verbose_name_plural': 'Записи'},
        ),
        migrations.AlterModelOptions(
            name='results',
            options={'verbose_name': 'Результат', 'verbose_name_plural': 'Результаты'},
        ),
    ]
