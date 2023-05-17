from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import MovieListSerializers

from .models import Movie
from ott.models import Netflix

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)

@api_view(['GET'])
def get_movie_details(request):
    netflix_movies = Netflix.objects.all()

    for movie in netflix_movies:
        tmdb_id = movie.tmdb_id  # tmdb_id 가져오기
        api_key = '5d5ba12807e444883a57039b0e2a1015'
        url = f'https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={api_key}'
        response = requests.get(url)
        if response.status_code == 200:  # 요청을 받으면
            movie_details = response.json()
            title = movie_details.get('title')
            overview = movie_details.get('overview')
            poster_path = movie_details.get('poster_path')
            release_date = movie_details.get('release_date')

            movie_obj, created = Movie.objects.get_or_create(title=title)
            movie_obj.overview = overview
            movie_obj.poster_path = poster_path
            movie_obj.release_date = release_date
            movie_obj.save()
    
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

