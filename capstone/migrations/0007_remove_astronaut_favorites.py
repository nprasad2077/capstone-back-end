# Generated by Django 4.1.4 on 2022-12-28 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0006_astronaut_favorites_alter_astronaut_planets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='astronaut',
            name='favorites',
        ),
    ]
