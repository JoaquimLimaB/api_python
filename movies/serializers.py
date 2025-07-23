from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


class MovieSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Movie
        fields = '__all__'

    #Validação de data de filme: OBS: obrigatorio 'validate_NOME_DO_CAMPO_VALIDADO'
    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError(
                'A data não pode ser inferior a 1900')
        return value

    #Validação da quantidade de caracteres:
    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError(
                'O resumo não deve conter mais de 500 caracteres')
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    #'read_only=True' --> significa que ele é apenas para leitura
    rate = serializers.SerializerMethodField(read_only=True)
    #Trazendo os dados de genres e não o id
    genre = GenreSerializer()
    #Trazendo os dados de actors e não o id, o many undica que pode ser uma lista com varios nomes 
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie 
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    #Calculando: campo calculado tem que ter: get_NomeDaVariavel
    def get_rate(self, obj):
        #Agregando o campo 'stars', ele pega a media(Avg)e agregada a reviews
       rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        #Se meu filme tiver alguma avaliação entra nesse 'if'
       if rate:
           return round(rate, 1)     
       return None


