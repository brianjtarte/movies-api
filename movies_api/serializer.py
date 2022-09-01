from rest_framework import serializers
from .models import Movies


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'description', 'created_at', 'updated_at')
        model = Movies
