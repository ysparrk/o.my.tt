from rest_framework import serializers
from .models import Movie, Tmdb

class TmdbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tmdb
        fields = '__all__'
