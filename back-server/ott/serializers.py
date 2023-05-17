from rest_framework import serializers
from .models import Netflix


class NetflixListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Netflix
        fields = '__all__'