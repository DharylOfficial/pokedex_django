from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from . import actions

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
