# Generated by Django 3.2.7 on 2021-10-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxis_vyzov', '0004_auto_20211002_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.TextField(),
        ),
    ]
