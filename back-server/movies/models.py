from django.db import models

# Create your models here.
class Movie(models.Model):
    cinema_release_date = models.DateField()
    full_path = models.CharField(max_length=255)
    full_paths = models.JSONField()
    id = models.IntegerField(primary_key=True)
    jw_entity_id = models.CharField(max_length=255)
    object_type = models.CharField(max_length=255)
    poster = models.CharField(max_length=255)
    poster_blur_hash = models.CharField(max_length=255)
    scoring = models.JSONField()
    title = models.CharField(max_length=255)

    # Add fields for other files here

    def __str__(self):
        return self.title
    

# class Netflix(models.Model):
#     id = models.IntegerField(primary_key=True)
#     tmdb_id = models.PositiveIntegerField()
#     title = models.CharField(max_length=255)

#     def __str__(self):
#         return self.title