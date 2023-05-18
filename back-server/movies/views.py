from django.shortcuts import render
import requests
import datetime
from django.views.decorators.http import require_safe
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import JsonResponse
from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TmdbSerializer, OttSerializer

from .models import Movie, Ott, Tmdb

# Create your views here.
# @api_view(['GET'])
# def tmdb_list(request):
#     tmdb_data = Tmdb.objects.all()
#     serializer = TmdbSerializer(tmdb_data, many=True)
#     return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = TmdbSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)


# ott 명단 보내기
@api_view(['GET'])
def ott_list(request):
    ott_data = Ott.objects.all()
    serializer = OttSerializer(ott_data, many=True)
    print('요청 보냄================')
    return Response(serializer.data)


@api_view(['GET'])
def tmdb_list(request, initial):

    print("요청받음!!=============")
    tmdb_data = Tmdb.objects.all()
    
    movie_list = []

    for movie in tmdb_data:
        m = movie.ott_lst

        for i in m:

            if i == initial:
                movie_list.append(movie)
    print(movie_list)
    serializer = TmdbSerializer(movie_list, many=True)
    return Response(serializer.data)




'''
def index(request):
    movie_list = Tmdb.objects.all()
    
    # Movie 모델에 데이터 넣기
    for movie in movie_list:
        tmdb_id = movie.tmdb_id  # tmdb_id 가져오기
        print(tmdb_id)
        api_key = '5d5ba12807e444883a57039b0e2a1015'
        url = f'https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={api_key}&language=ko-KR'
        response = requests.get(url)
        if response.status_code == 200:  # 요청을 받으면
            movie_details = response.json()
            title = movie_details.get('title')
            overview = movie_details.get('overview')
            poster_path = movie_details.get('poster_path')
            release_date_str = movie_details.get('release_date')
            if release_date_str:
                release_date = datetime.datetime.strptime(release_date_str, '%Y-%m-%d').date()
            else:
                release_date = None

        movie_obj, created = Movie.objects.get_or_create(title=title)
        movie_obj.overview = overview
        movie_obj.poster_path = poster_path
        movie_obj.release_date = release_date
        movie_obj.save()

        movie_obj.otts.add(movie)
    
    movies = Movie.objects.all()
    print(movies)
    
    context = {
        # 'otts': otts,
        # 'movie_list': movies,
        'movies' : movies,
    }

    # otts = Ott.objects.all()

    # # 필터링
    # ott_initial = None
    # try:
    #     ott = Ott.objects.get(pk=ott_pk)
    #     ott_initial = ott.initial
    # except Ott.DoesNotExist:
    #     pass

    # movie_list = []
    # tmdb_ids = Tmdb.objects.filter(ott__initial=ott_initial).values_list('tmdb_id', flat=True)
    # movies = movies.filter(tmdb__tmdb_id__in=tmdb_ids)

    # context = {
    #     'otts': otts,
    #     'movie_list': movies,
    #     'movies' : movies,
    # }
    return render(request, 'movies/index.html', context)


    # sorted(movie_list, key=lambda movie: movie.ott)  # 일단 이름순으로 정렬



@require_safe
def ott_filter(request, ott_pk):
    otts = Ott.objects.all()
    movies = Movie.objects.all()

    ott_initial = None
    try:
        ott = Ott.objects.get(pk=ott_pk)
        ott_initial = ott.initial
    except Ott.DoesNotExist:
        pass

    movie_list = []
    tmdb_ids = Tmdb.objects.filter(ott__initial=ott_initial).values_list('tmdb_id', flat=True)
    movies = movies.filter(tmdb__tmdb_id__in=tmdb_ids)

    context = {
        'otts': otts,
        'movie_list': movies,
    }
    return render(request, 'movies/index.html', context)

# api 요청 보내서 db에 영화 정보 저장
# @api_view(['GET'])
# def get_movie_details(request):
#     netflix_movies = Netflix.objects.all()

    # for movie in netflix_movies:
    #     tmdb_id = movie.tmdb_id  # tmdb_id 가져오기
    #     api_key = '5d5ba12807e444883a57039b0e2a1015'
    #     url = f'https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={api_key}'
    #     response = requests.get(url)
    #     if response.status_code == 200:  # 요청을 받으면
    #         movie_details = response.json()
    #         title = movie_details.get('title')
    #         overview = movie_details.get('overview')
    #         poster_path = movie_details.get('poster_path')
    #         release_date = movie_details.get('release_date')

    #         movie_obj, created = Movie.objects.get_or_create(title=title)
    #         movie_obj.overview = overview
    #         movie_obj.poster_path = poster_path
    #         movie_obj.release_date = release_date
    #         movie_obj.save()
    
#     movies = Movie.objects.all()
#     serializer = MovieSerializer(movies, many=True)
#     return Response(serializer.data)

# 포스터 사진 누르면 movie detail 나온다. -> 이때 api 요청 후 받아오기..??
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


def recommended(request):
    pass
'''