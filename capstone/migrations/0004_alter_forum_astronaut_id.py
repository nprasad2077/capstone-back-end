# Generated by Django 4.1.4 on 2022-12-28 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0003_forum_astronaut_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='astronaut_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forums', to='capstone.astronaut'),
        ),
    ]
