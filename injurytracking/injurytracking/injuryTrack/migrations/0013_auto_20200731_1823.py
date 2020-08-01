# Generated by Django 3.0.8 on 2020-07-31 18:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('injuryTrack', '0012_auto_20200731_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='addedOn',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 18, 23, 0, 405789, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='completedOn',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='injury',
            name='addedOn',
            field=models.DateTimeField(default=datetime.date(2020, 7, 31)),
        ),
        migrations.AlterField(
            model_name='injury',
            name='removedOn',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='injury',
            name='updatedOn',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
