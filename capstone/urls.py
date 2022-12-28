# tunr/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.astronaut_list, name='astronaut_list'),
    path('forums/', views.forum_list, name='forum_list'),
    path('astronauts/<int:pk>', views.astronaut_detail, name='astronaut_detail'),
    path('forums/<int:pk>', views.forum_detail, name='forum_detail'),
    path('astronauts/new', views.astronaut_create, name='astronaut_create'),
    path('forums/new', views.forum_create, name='forum_create'),
]
