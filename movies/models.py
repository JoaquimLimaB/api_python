from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=500)
    # Interligando meus models de genre a este campo // este on_delete não deixa eu excluir um genereo caso ele esteja em uso
    genre = models.ForeignKey(
        Genre, on_delete=models.PROTECT, related_name='movies')
    release_date = models.DateField(null=True, blank=True)
    # O 'ManyToManyFiel', permite que eu coloque varios atores ligados ao filme, por isso não fiz'ForeignKey'
    actors = models.ManyToManyField(Actor, related_name='movies')
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
