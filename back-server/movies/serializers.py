from rest_framework import serializers
from .models import Movie, Tmdb, Ott

class TmdbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tmdb
        fields = '__all__'

# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ['tmdb_id', 'ott_lst']

class OttSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ott
        fields = '__all__'