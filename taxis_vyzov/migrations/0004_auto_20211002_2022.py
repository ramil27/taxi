# Generated by Django 3.2.7 on 2021-10-02 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxis_vyzov', '0003_auto_20211001_1931'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='YandexCar',
        ),
    ]