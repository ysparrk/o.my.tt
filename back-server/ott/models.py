from django.db import models

# Create your models here.
class Netflix(models.Model):
    full_path = models.CharField(max_length=200)
    full_paths = models.JSONField(default=dict)
    jw_entity_id = models.CharField(max_length=20)
    object_type = models.CharField(max_length=20)
    poster = models.CharField(max_length=200)
    poster_blur_hash = models.CharField(max_length=100)
    scoring = models.JSONField()
    title = models.CharField(max_length=100)
    tmdb_id = models.IntegerField(null=True)  # 새로운 필드 추가

    def get_tmdb_id(self):
        for score in self.scoring:
            if score.get("provider_type") == "tmdb:id":
                return score.get("value")
        return None