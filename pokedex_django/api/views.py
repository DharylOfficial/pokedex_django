from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from pokemon.models import Type, Pokemon
from pokemon.serializers import TypeSerializer, PokemonSerializer

# Create your views here.
class PokemonViewSet(ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class TypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer