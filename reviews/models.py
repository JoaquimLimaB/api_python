from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.PROTECT, related_name='reviews')
    # Validando minhas stars que so podem variar de 0 ate 5 --> Import 'from django.core.validatorsport ......'
    stars = models.IntegerField(
        validators=[
            MinValueValidator(
                0, 'Erro: o número não pode ser inferior a zero estrelas'),
            MaxValueValidator(
                5, 'Erro: o número não pode ser supeior a cinco estrelas'),
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):  # 135
        return self.movie.title
