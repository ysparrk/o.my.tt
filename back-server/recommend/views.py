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
    random_data = random.sample(movie_data, 5)
    print(random_data)
    
    serializer = MovieSerializer(random_data, many=True)

    return Response(serializer.data)


# @api_view(['POST'])
# def get_select_id(request):
#     selectedId = request.data.get(selectedId)
#     pass



# 최적의 ott 추천하는 알고리즘
# @api_view(['GET', 'POST'])
# def optimize_ott(request):

#     '''
#     2. 선택한 영화를 for문으로 돌면서 initial 값 확인 -> pk 값에 따라 +1 증가시키기
#     3. 최대 점수를 가진 것 출력
#     '''
#     ott_data = Ott.objects.all()
#     print('응답 들어옴')
#     # print(request.data)

#     # print(request.data['payload'])
#     # print(type(request.data['payload']))
#     plus = [0] * 6
#     lst = request.data['payload']
    
#     for i in lst:
#         movie = Tmdb.objects.get(i)
#         ott_lst = movie.ott_lst
#         # print(m)
        
#         # 해당 영화의 ott_lst 가져오기 -> for 문 돌려서 해당하는 ott 찾기
#         for j in ott_lst:
            

#     serializer = OttSerializer(recommended_ott)

#     return Response(serializer.data)

@api_view(['GET', 'POST'])
def optimize_ott(request):

    print('응답 받음!!')
    print(request.data['payload'])
    ott_data = Ott.objects.all()
    tmdb_ids = request.data['payload']  # 받은 tmdb_id 값
    ott_counts = [0] * 6  # 여기에 pk값으로 들어갈 것임

    for tmdb_id in tmdb_ids:
        print(tmdb_id)
        movie = Tmdb.objects.get(pk=tmdb_id)

        # movie = get_object_or_404(Tmdb, pk=tmdb_id)
        ott_lst = movie.ott_lst  # 그 영화의 ott_lst
        print(ott_lst)
        for ott_initial in ott_lst:
            ott_counts[ott_initial] += 1

    most_common_ott_pk = ott_counts.index(max(ott_counts)) + 1
    recommended_ott = get_object_or_404(Ott, pk=most_common_ott_pk)
    print(recommended_ott)

    serializer = OttSerializer(recommended_ott)
    
    return Response(serializer.data)


