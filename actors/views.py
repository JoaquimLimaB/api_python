from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from actors.models import Actor
from actors.serializers import ActorSerializer
from app.permissions import GlobalDefaultPermission


class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,) # Para esse recurso ficar disponivel tem que passar pela "IsAuthenticated"(ter o token). Da certo com lista[] e tupla()
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,) 
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
