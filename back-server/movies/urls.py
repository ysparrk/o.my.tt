from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('ott/', views.ott_list, name='ott_list'),
<<<<<<< HEAD
    path('tmdb/<str:initial>', views.tmdb_list, name='tmdb_lis'),
=======
    path('tmdb/<str:initial>', views.tmdb_movie_list, name='tmdb_movie_list'),
>>>>>>> ott_button
]
