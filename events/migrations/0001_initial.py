# Generated by Django 3.2.13 on 2022-05-06 01:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('desc', models.TextField(verbose_name='Название')),
                ('user_id', models.IntegerField(verbose_name='user_id')),
                ('thumb', models.CharField(max_length=128, verbose_name='Название')),
                ('x', models.FloatField(verbose_name='y')),
                ('y', models.FloatField(verbose_name='y')),
                ('status', models.CharField(max_length=64, verbose_name='status')),
                ('acesss', models.CharField(max_length=64, verbose_name='acess')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='date')),
                ('start_time', models.TimeField(blank=True, null=True, verbose_name='From')),
                ('end_time', models.TimeField(blank=True, null=True, verbose_name='End')),
            ],
        ),
    ]