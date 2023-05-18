from django.urls import path
from . import views

app_name = 'recommend'
urlpatterns = [
    path('random/', views.random_tmdb, name='random_tmdb'),
]