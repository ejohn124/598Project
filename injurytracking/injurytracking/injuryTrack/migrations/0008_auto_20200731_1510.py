# Generated by Django 3.0.8 on 2020-07-31 15:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('injuryTrack', '0007_auto_20200731_1508'),
    ]

    operations = [
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