from django import forms
from .models import Astronaut, Forum

class AstronautForm(forms.ModelForm):

    class Meta:
        model = Astronaut
        fields = ('name', 'favorite_planet', 'photo_url', 'planets')

class ForumForm(forms.ModelForm):

    class Meta:
        model = Forum
        fields = ('title', 'photo', 'preview_url')