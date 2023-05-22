from django.shortcuts import render
import requests
import datetime
from django.views.decorators.http import require_safe
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import JsonResponse
from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import api_view

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import TmdbSerializer, OttSerializer, MovieSerializer, CommentSerializer, MovieDetailSerializer, SearchSerializer

from .models import Movie, Ott, Tmdb, Comment

# Create your views here.

# 1. ott filter button
# ott 명단 보내기
@api_view(['GET'])
def ott_list(request):
    ott_data = Ott.objects.all()
    serializer = OttSerializer(ott_data, many=True)
    # print('요청 보냄================')
    return Response(serializer.data)

# ott 버튼 누르면 해당 ott 영화 보내기
@api_view(['GET'])
def tmdb_movie_list(request, initial):

    # print("요청받음!!=============")
    # print(initial)
    tmdb_data = Tmdb.objects.all()
    # movie_data = Movie.objects.all()
    # print(movie_data)
    movie_list = []

    for movie in tmdb_data:
        m = movie.ott_lst
        
        if initial in m:  # ott 값이 포함된 경우
            rlt = movie.tmdb_id

            # print(rlt)
            movie_list.append(rlt)
    
    # print(movie_list)
    serializer = MovieSerializer(movie_list, many=True)

    return Response(serializer.data)


# movie_detail
@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    print("detail 요청 받음")
    serializer = MovieDetailSerializer(movie)
    print(serializer.data)
    return Response(serializer.data)


# likes
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def likes(request, movie_id):
    print("좋아요 요청 받음")
    movie = get_object_or_404(Movie, id=movie_id)
    user = request.user
    
    if movie.like_users.filter(id=user.id).exists():
        # 이미 좋아요를 누른 경우, 좋아요 취소
        movie.like_users.remove(user)
        liked = False
        print(liked)
    else:
        # 좋아요를 누르지 않은 경우, 좋아요 추가
        movie.like_users.add(user)
        liked = True
        print(liked)

    # 좋아요 개수 업데이트
    likes_count = movie.like_users.count()
    movie.likes_count = likes_count
    movie.save()

    return Response({'liked': liked, 'likes_count': likes_count})

# comments
@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def comment_create(request, movie_id):
    print("댓글 받음")
    print(request.data)
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        print("댓글 조회 요청 들어옴")
        comments = Comment.objects.filter(movie=movie)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#######################################################
###################### { 검색어 } ######################
@api_view(['GET'])
def search_movies(request, query):
    movies = Movie.objects.filter(title__icontains=query)

    movie_info = [{'id': movie.id, 'title': movie.title, 'poster_path': movie.poster_path} for movie in movies]
    # print(movie_info)

    serializer = SearchSerializer(movie_info, many=True)

    return Response(serializer.data)
#######################################################
#######################################################




