# tunr/urls.py
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('astronauts/', views.AstronautList.as_view(), name='astonaut_list'),
    path('astronauts/<int:pk>', views.AstronautDetail.as_view(), name='astronaut_detail'),
    path('forums/', views.ForumList.as_view(), name="forum_list"),
    path('forums/<int:pk>', views.ForumDetail.as_view(), name="forum_detail"),
]
