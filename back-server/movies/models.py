from django.db import models

# Create your models here.

class Ott(models.Model):
    initial = models.CharField(max_length=50)
    name = models.CharField(max_length=50) 

class Tmdb(models.Model):
    tmdb_id = models.IntegerField()
    ott_lst = models.JSONField()
    

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    adult = models.BooleanField()
    title = models.CharField(max_length=100)
    overview = models.TextField(null=True, blank=True)
    poster_path = models.TextField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    backdrop_path = models.TextField(null=True, blank=True)
    popularity = models.FloatField()
    tagline = models.CharField(max_length=255)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()

    def __str__(self):
        return self.title

