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

# ott 명단 보내기
@api_view(['GET'])
def ott_list(request):
    ott_data = Ott.objects.all()
    serializer = OttSerializer(ott_data, many=True)
    print('요청 보냄================')
    return Response(serializer.data)

# ott 버튼 누르면 해당 ott 영화 보내기
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
