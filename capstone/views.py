# views.py
from rest_framework import generics
from .serializers import AstronautSerializer, ForumSerializer
from .models import Astronaut, Forum

class AstronautList(generics.ListCreateAPIView):
    queryset = Astronaut.objects.all()
    serializer_class = AstronautSerializer

class AstronautDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Astronaut.objects.all()
    serializer_class = AstronautSerializer

class ForumList(generics.ListCreateAPIView):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer

class ForumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer
