from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Astronaut(models.Model):
    name = models.CharField(max_length=100)
    favorite_planet = models.CharField(max_length=100)
    photo_url = models.TextField()
    planets = ArrayField(models.CharField(max_length=100, blank=True))


    def __str__(self):
        return self.name

