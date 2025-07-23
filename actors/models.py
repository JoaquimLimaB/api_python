from django.db import models

# Colocar as nacionalidades que deve aparecer no compo Nationality.
NATIONALITY_CHOICES = (
    # Valor a esquerda é que sera saldo no BC, o da direita é que vai mostrar pro User:
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
