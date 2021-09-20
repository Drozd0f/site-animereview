from rest_framework import serializers

from reviews.models import Posts, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['pk', 'name', 'slug']


class PostsSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    universe = serializers.StringRelatedField()

    class Meta:
        model = Posts
        fields = ['id', 'title', 'text', 'photo', 'rating', 'universe', 'genre']
        # exclude = ('user', 'slug')
