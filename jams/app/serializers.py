from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class Playlist(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = "__all__"

class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=True)
    genre = GenreSerializer(many=True)
    # user = UserSerializer(many=True)
    album = AlbumSerializer()
    class Meta:
        model = Song
        fields = "__all__"