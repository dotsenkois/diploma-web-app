# Generated by Django 3.2.7 on 2021-11-28 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0007_auto_20211128_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='month',
        ),
        migrations.RemoveField(
            model_name='results',
            name='month',
        ),
    ]