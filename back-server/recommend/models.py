from django.db import models

# Create your models here.
class Info(models.Model):
    already = models.JSONField(null=True, blank=True)  # 이미 가지고 있는 OTT
    prefer = models.JSONField(null=True, blank=True) # 원하는 영화
