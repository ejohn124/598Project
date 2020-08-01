# Generated by Django 3.0.8 on 2020-07-30 23:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('injuryTrack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ATC',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('sport', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('emergency_contact', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Injury',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('atc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='injuryTrack.ATC')),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='injuryTrack.Athlete')),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sets', models.IntegerField(default=0)),
                ('reps', models.IntegerField(default=0)),
                ('duration', models.DurationField()),
                ('injury', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='injuryTrack.Injury')),
            ],
        ),
        migrations.AddField(
            model_name='athlete',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='injuryTrack.School'),
        ),
        migrations.AddField(
            model_name='atc',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='injuryTrack.School'),
        ),
    ]