from django.urls import path
from movies.views import index, get_movie_details

urlpatterns = [
    path('', index, name='index'),
    path('get-movie-details/', get_movie_details, name='get_movie_details'),
]
