# Generated by Django 3.2.7 on 2021-10-05 08:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 5, 8, 28, 44, 648486, tzinfo=utc)),
        ),
    ]
