from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pokemon.models import Type, Pokemon
from pokemon.serializers import TypeSerializer, PokemonSerializer
from pokemon.actions import resetPokedex

# Create your views here.
class PokemonViewSet(ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class TypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    
@api_view(["POST"])
def resetPokedexEndpoint(request):
    print(request.data['reset'])
    if (request.data['reset']):
        resetPokedex()
        return Response(None, status=status.HTTP_205_RESET_CONTENT)
    return Response(None, status=status.HTTP_400_BAD_REQUEST)