from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('ott/', views.ott_list, name='ott_list'),
    path('tmdb/<str:initial>', views.tmdb_movie_list, name='tmdb_movie_list'),
]
