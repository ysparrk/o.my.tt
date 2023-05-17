from django.shortcuts import render
import requests
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
        response = requests.get(url)
        if response.status_code == 200:
            movie_details = response.json()
            # 여기에서 필요한 정보를 추출하여 처리하면 됩니다
            # 예시로 영화 제목과 개요를 출력해봅니다
            movie_obj, created = Movie.objects.get_or_create(id=movie.id)
            movie_obj.title = title
            # 필요한 정보 추가적으로 저장
            print(movie_details['title'])
            movie_obj.save()
            print(f"Movie details updated for: {movie_obj.title}")

    return render(request, 'movies/detail.html')

# def fetch_movie_details(movie):
#     netflix_movies = Netflix.objects.all()
#     tmdb_id = netflix_movies.get.tmdb_id()
#     api_key = '5d5ba12807e444883a57039b0e2a1015'
#     url = f'https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={api_key}'

#     response = requests.get(url)
#     if response.status_code == 200:
#         movie_data = response.json()
#         # 필요한 정보를 추출하여 Movie 객체의 필드에 저장
#         movie.cinema_release_date = movie_data['release_date']
#         # 필요한 정보 추가적으로 저장
        
#         movie.save()
#         print(f"Movie details updated for: {movie.title}")
