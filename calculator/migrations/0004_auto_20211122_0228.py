# Generated by Django 3.2.7 on 2021-11-22 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_results'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Вахта', 'verbose_name_plural': 'Вахта'},
        ),
        migrations.AddField(
            model_name='profile',
            name='Обсервация',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='results',
            name='observation',
            field=models.IntegerField(default=0, verbose_name='Обсервация'),
            preserve_default=False,
        ),
    ]
