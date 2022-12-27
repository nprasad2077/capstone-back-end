# tunr/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.astronaut_list, name='astronaut_list'),
    path('forums/', views.forum_list, name='forum_list'),
]
