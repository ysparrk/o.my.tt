from django.db import models

# Create your models here.
# 전체 영화 리스트
class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.TextField()
    release_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.title
