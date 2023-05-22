from rest_framework import serializers
from .models import Movie, Tmdb, Ott, Comment

class TmdbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tmdb
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'poster_path',)


#######################################################
###################### { 검색어 } ######################
class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path',)
#######################################################
#######################################################

class OttSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ott
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# MovieDetail 
class MovieDetailSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_likes_count(self, instance):
        return instance.like_users.count()

    def get_comments(self, instance):
        comments = Comment.objects.filter(movie=instance)
        serializer = CommentSerializer(comments, many=True)
        return serializer.data

