from django.shortcuts import render
from .models import Astronaut, Forum

def astronaut_list(request):
    astronauts = Astronaut.objects.all()
    return render(request, 'capstone/astronaut_list.html', {'astronauts': astronauts})

def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'capstone/forum_list.html', {'forums': forums})
