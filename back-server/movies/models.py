from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.TextField()
    release_date = models.DateField()
    
    def __str__(self):
        return self.title

# class Netflix(models.Model):
#     id = models.IntegerField(primary_key=True)
#     tmdb_id = models.PositiveIntegerField()
#     title = models.CharField(max_length=255)

#     def __str__(self):
#         return self.title