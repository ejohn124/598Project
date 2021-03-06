# Generated by Django 3.0.8 on 2020-07-31 13:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('injuryTrack', '0003_auto_20200731_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='addedOn',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 13, 8, 23, 125175, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='exercise',
            name='completedOn',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='injury',
            name='addedOn',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 13, 8, 23, 124507, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='injury',
            name='updatedOn',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
