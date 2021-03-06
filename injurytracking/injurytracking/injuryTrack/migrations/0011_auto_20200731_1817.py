# Generated by Django 3.0.8 on 2020-07-31 18:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('injuryTrack', '0010_auto_20200731_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='addedOn',
            field=models.DateField(default=datetime.date(2020, 7, 31)),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='completedOn',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='injury',
            name='addedOn',
            field=models.DateField(default=datetime.date(2020, 7, 31)),
        ),
        migrations.AlterField(
            model_name='injury',
            name='removedOn',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='injury',
            name='updatedOn',
            field=models.DateField(blank=True, null=True),
        ),
    ]
