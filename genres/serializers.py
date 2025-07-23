from rest_framework import serializers
from genres.models import Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'  # Posso devolver somente o campo name: fields = ['name']
