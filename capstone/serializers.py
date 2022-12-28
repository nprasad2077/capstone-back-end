from rest_framework import serializers
from .models import Astronaut, Forum

class AstronautSerializer(serializers.HyperlinkedModelSerializer):
    forums = serializers.HyperlinkedRelatedField(
        view_name='forum_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Astronaut
        fields = ('id', 'name', 'favorite_planet', 'photo_url', 'planets',)

class ForumSerializer(serializers.HyperlinkedModelSerializer):
    astronaut = serializers.HyperlinkedRelatedField(
        view_name='astronaut_detail',
        read_only=True
    )
    astronaut_id = serializers.PrimaryKeyRelatedField(
        queryset=Astronaut.objects.all(),
        source='astronaut'
    )
    class Meta:
        model = Forum
        fields = ('id', 'astronaut','astronaut_id', 'title', 'photo', 'preview_url',)
