# Generated by Django 3.0.8 on 2020-07-31 16:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('injuryTrack', '0009_auto_20200731_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='addedOn',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 16, 20, 39, 737614, tzinfo=utc)),
        ),
    ]
