# Generated by Django 3.2.6 on 2021-08-30 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_reviewmodel_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizamodel',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pizamodel',
            name='number_rating',
            field=models.IntegerField(default=0),
        ),
    ]
