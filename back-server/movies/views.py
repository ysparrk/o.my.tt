from django.shortcuts import render
import requests
import datetime
from django.views.decorators.http import require_safe
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import JsonResponse
from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TmdbSerializer, OttSerializer, MovieSerializer

from .models import Movie, Ott, Tmdb

# Create your views here.

# 1. ott filter button
# ott 명단 보내기
@api_view(['GET'])
def ott_list(request):
    ott_data = Ott.objects.all()
    serializer = OttSerializer(ott_data, many=True)
    print('요청 보냄================')
    return Response(serializer.data)

# ott 버튼 누르면 해당 ott 영화 보내기
@api_view(['GET'])
def tmdb_movie_list(request, initial):

    print("요청받음!!=============")
    print(initial)
    tmdb_data = Tmdb.objects.all()
    # movie_data = Movie.objects.all()
    # print(movie_data)
    movie_list = []

    for movie in tmdb_data:
        m = movie.ott_lst
        
        if initial in m:  # ott 값이 포함된 경우
            rlt = movie.tmdb_id

            print(rlt)
            movie_list.append(rlt)
    
    print(movie_list)
    serializer = MovieSerializer(movie_list, many=True)
    return Response(serializer.data)


# likes
@api_view(['POST'])
def likes(request, movie_pk):
    pass
    # if request.user.is_authenticated: # 로그인 한 사람만 가능
    #     article = Article.objects.get(pk=article_pk)
        
    #     # 이 article의 모든 좋아요를 누른 user중에 request한 user가 있다면(이미 누른 상태)
    #     if article.like_users.filter(pk=request.user.pk).exists():
    #         article.like_users.remove(request.user)  # 좋아요 취소

    #     else:
    #         article.like_users.add(request.user)  # 좋아요 목록에 더해주기
    #     return redirect('articles:index')  # 글 목록으로 돌아가기
    
    # return redirect('accounts:login')  # 로그인 하지 않았다면 로그인 창으로 가기
