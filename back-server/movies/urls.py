from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # path('', views.index, name='index'), # 전체 영화 목록 페이지 조회
    # path('tmdb/', views.tmdb_list, name='tmdb_list'),
    # path('ott/', views.ott_list, name='ott_list'),
    path('ott/<str:initial>', views.ott_list, name='ott_list'),
    # path('<int:movie_pk>/', views.detail, name='detail'), # 단일 영화 상세 페이지
    # path('get-movie-details/', views.get_movie_details, name='get_movie_details'),
]
