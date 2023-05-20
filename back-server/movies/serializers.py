from rest_framework import serializers
from .models import Movie, Tmdb, Ott

class TmdbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tmdb
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class OttSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ott
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='movie.like_users', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_users',)