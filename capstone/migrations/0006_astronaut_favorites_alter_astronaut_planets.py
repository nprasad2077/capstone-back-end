# Generated by Django 4.1.4 on 2022-12-28 16:44

import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0005_forum'),
    ]

    operations = [
        migrations.AddField(
            model_name='astronaut',
            name='favorites',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500, null=True), default=django.utils.timezone.now, size=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='astronaut',
            name='planets',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='no planets', max_length=100), size=None),
        ),
    ]
