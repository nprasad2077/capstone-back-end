# Generated by Django 4.1.4 on 2022-12-28 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='astronaut',
        ),
    ]
