from django.shortcuts import render, redirect
from .models import Astronaut, Forum
from .forms import AstronautForm, ForumForm

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

def astronaut_create(request):
    if request.method == 'POST':
        form = AstronautForm(request.POST)
        if form.is_valid():
            astronaut = form.save()
            return redirect('astronaut_detail', pk=astronaut.pk)
    else:
        form = AstronautForm()
    return render(request, 'capstone/astronaut_form.html', {'form': form})

def forum_create(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            forum = form.save()
            return redirect('forum_detail', pk=forum.pk)
    else:
        form = ForumForm()
    return render(request, 'capstone/forum_form.html', {'form': form})

def astronaut_edit(request, pk):
    astronaut = Astronaut.objects.get(pk=pk)
    if request.method == 'POST':
        form = AstronautForm(request.POST, instance=astronaut)
        if form.is_valid():
            astronaut = form.save()
            return redirect('astronaut_detail', pk=astronaut.pk)
    else:
        form = AstronautForm(instance=astronaut)
    return render (request, 'capstone/astronaut_form.html', {'form': form})

def forum_edit(request, pk):
    forum = Forum.objects.get(pk=pk)
    if request.method == 'POST':
        form = ForumForm(request.POST, instance=forum)
        if form.is_valid():
            forum = form.save()
            return redirect('forum_detail', pk=forum.pk)
    else:
        form = ForumForm(instance=forum)
    return render(request, 'capstone/forum_form.html', {'form': form})

def astronaut_delete(request, pk):
    Astronaut.objects.get(id=pk).delete()
    return redirect('astronaut_list')

def forum_delete(request, pk):
    Forum.objects.get(id=pk).delete()
    return redirect('forum_list')
        