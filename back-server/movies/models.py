from django.db import models

# Create your models here.

class Ott(models.Model):
    initial = models.CharField(max_length=50)
    name = models.CharField(max_length=50) 

class Tmdb(models.Model):
    tmdb_id = models.IntegerField()
    ott_lst = models.CharField(max_length=20)

    # def __str__(self):
    #     return str(self.tmdb_id)
    
# DB에 저장
class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(null=True, blank=True)
    poster_path = models.TextField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    otts = models.ManyToManyField(Tmdb)

    def __str__(self):
        return self.title
