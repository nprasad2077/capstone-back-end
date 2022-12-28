from django import forms
from .models import Astronaut, Forum

class AstronautForm(forms.ModelForm):

    class Meta:
        model = Astronaut
        fields = ('name', 'favorite_planet', 'photo_url', 'planets', 'favorites')