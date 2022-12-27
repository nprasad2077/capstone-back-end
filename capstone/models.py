from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Astronaut(models.Model):
    name = models.CharField(max_length=100)
    favorite_planet = models.CharField(max_length=100)
    photo_url = models.TextField()
    planets = ArrayField(models.CharField(max_length=100, blank=True))
    favorites: ArrayField(models.CharField(max_length=500, blank=True))

    def __str__(self):
        return self.name


class Forum(models.Model):
    astronaut = models.ForeignKey(Astronaut, on_delete=models.CASCADE, related_name='forums')
    title = models.CharField(max_length=100, default='no title')
    photo = models.CharField(max_length=100, default='no photo')
    preview_url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title

