from django.shortcuts import render
# import requests
from .models import Movie
from ott.models import Netflix

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)


def get_movie_details(request):
    netflix_movies = Netflix.objects.all()

    for movie in netflix_movies:
        tmdb_id = movie.tmdb_id
        api_key = '5d5ba12807e444883a57039b0e2a1015'
        url = f'https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={api_key}'
        response = request.get(url)
        if response.status_code == 200:
            movie_details = response.json()
            # 여기에서 필요한 정보를 추출하여 처리하면 됩니다
            # 예시로 영화 제목과 개요를 출력해봅니다
            print(movie_details['title'])
            print(movie_details['overview'])

    return render(request, 'movies/detail.html')
