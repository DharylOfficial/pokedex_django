from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from . import actions

from .models import Type
from .serializers import PokemonSerializer

# Create your views here.


def index(request):
    return HttpResponse("Route to /pokemon/pull to transfer data from Official Pokedex to your Pokedex")


def pullAll(request):
    types = actions.pullAll()
    
    return HttpResponse("Data from Official Pokedex Retrieved")


def pullTypes(request):
    types = actions.pullTypes()
    
    return HttpResponse("Types from Official Pokedex Retrieved")


def pullPokemon(request):
    types = actions.pullPokemon()
    
    return HttpResponse("Pokemon from Official Pokedex Retrieved")

def getTypes(request):
    types = actions.getTypes()
    
    return HttpResponse("Printing Types already in Database")


# Create experimental views here.

# Returns JSON of list of all Pokemon with type 1: Normal
def test_type_normal(request):
    type_normal = Type.objects.get(pk=1)    
    pokemon = type_normal.pokemon_set.all().values()
    pokemon_list = list(pokemon)
    
    return JsonResponse(pokemon_list, safe=False)