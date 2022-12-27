from django.shortcuts import render
from .models import Astronaut, Forum

def astronaut_list(request):
    astronauts = Astronaut.objects.all()
    return render(request, 'capstone/astronaut_list.html', {'astronauts': astronauts})

def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'capstone/forum_list.html', {'forums': forums})

def astronaut_detail(request, pk):
    astronaut = Astronaut.objects.get(id=pk)
    return render(request, 'capstone/astronaut_detail.html', {'astronaut': astronaut})

def forum_detail(request, pk):
    forum = Forum.objects.get(id=pk)
    return render(request, 'capstone/forum_detail.html', {'forum': forum})
