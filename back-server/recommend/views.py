from django.shortcuts import render, get_object_or_404
from collections import Counter
from movies.models import Tmdb, Movie, Ott
from .models import Info
from movies.serializers import TmdbSerializer, MovieSerializer, OttSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404, get_list_or_404
import random
# Create your views here.

# 전체 영화 중 특정 영화 10개 선택해서 보내기
@api_view(['GET'])
def random_tmdb(request):
    movie_data = list(Movie.objects.all())

    # n개 랜덤으로 추출
    random_data = random.sample(movie_data, 10)
    # print(random_data)
    
    serializer = MovieSerializer(random_data, many=True)

    return Response(serializer.data)


# 최적의 ott 추천
@api_view(['GET', 'POST'])
def optimize_ott(request):

    print('응답 받음!!')
    print(request.data['payload'])
    # ott_data = Ott.objects.all()
    tmdb_ids = request.data['payload']  # 받은 tmdb_id 값
    ott_counts = [0] * 6  # 여기에 pk값으로 들어갈 것임

    otts = {
        "nfx" : 0,
        "wac" : 1,
        "wav" : 2,
        "ply" : 3,
        "apt" : 4,
        "dnp" : 5,
    }

    for tmdb_id in tmdb_ids:
        print(tmdb_id)
        movie = get_object_or_404(Tmdb, pk=tmdb_id)
        print(f'선택된 영화 {movie}')

        ott_lst = movie.ott_lst  # 그 영화의 ott_lst

        # 해당되는 ott의 pk값 찾기
        for ott_initial in ott_lst:
            ott_counts[otts.get(ott_initial)] += 1

    # max_count = max(ott_counts)  # 최대값
    # max_indexes = [i for i, count in enumerate(ott_counts) if count == max_count]  # 최대값을 가진 인덱스들

    # final_recommend = Ott.objects.filter(pk__in=[index+1 for index in max_indexes])
    # print(final_recommend)

    # serializer = OttSerializer(final_recommend, many=True)

    # return Response(serializer.data)   

    # # print(f'count : {ott_counts}')

    rlt = ott_counts.index(max(ott_counts))  # 리스트에서 최댓값 인덱스 추출
    # print(f'rlt : {rlt}')
    final_recommend = Ott.objects.get(pk=(rlt+1))
    print(final_recommend)
    
    serializer = OttSerializer(final_recommend)
    
    return Response(serializer.data)


