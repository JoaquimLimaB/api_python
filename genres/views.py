from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.models import Genre
from genres.serializers import GenreSerializer
from app.permissions import GlobalDefaultPermission


# Lista de pordutos 'GET', e faz um 'POST'
class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,) # Para esse recurso ficar disponivel tem que passar pela "IsAuthenticated"(ter o token). Da certo com lista[] e tupla()
    queryset = Genre.objects.all()  # Minha tabela
    serializer_class = GenreSerializer

# Deleta, altera e pesquisa por ID
class GenereRetriveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

