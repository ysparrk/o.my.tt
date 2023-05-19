from django.shortcuts import render
from movies.models import Tmdb
from .models import Info
from movies.serializers import TmdbSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404, get_list_or_404
import random
# Create your views here.

# 전체 영화 중 특정 영화 10개 선택해서 보내기
@api_view(['GET'])
def random_tmdb(request):
    tmdb_data = list(Tmdb.objects.all())
    print('========================')
    print(tmdb_data)

    # n개 랜덤으로 추출
    random_data = random.sample(tmdb_data, 5)
    print(random_data)
    
    serializer = TmdbSerializer(random_data, many=True)

    return Response(serializer.data)


# 최적의 ott 추천하는 알고리즘
@api_view(['GET'])
def optimal_ott(request):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    info = Info.objects.all()  # 전체 가져오기
    ott_list = [0] * 5
    '''
    1. 이미 가지고 있는 ott 확인해서 제외하기
    2. 선택한 영화를 for문으로 돌면서 initial 값 확인 -> pk 값에 따라 +1 증가시키기
    3. 최대 점수를 가진 것 출력
    '''
    pass


