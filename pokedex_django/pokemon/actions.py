from .models import Type, Pokemon
import requests

def resetPokedex():
    deleteAll()
    pullAll()
    print("Pokedex reset successfully")

def pullAll():
    pullTypes()
    pullPokemon()
    print("Pulled all Pokemon from the API")
        
def deleteAll():
    deleteAllPokemon()
    deleteAllTypes()
    print("Deleted all Data in the Database")

def pullTypes():
    entire_types_url = "https://pokeapi.co/api/v2/type"
    response = requests.get(entire_types_url)
    types = response.json()
    
    for pokemon_type in types['results']:
        response = requests.get(pokemon_type['url'])
        data = response.json()
        
        t = Type(id=data['id'], name=data['name'])
        t.save()
        
        print(f"Added: {t}")
        
def pullPokemon():
    NO_OF_POKEMON = 151
    
    for pokemon_id in range(1, NO_OF_POKEMON + 1):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
        response = requests.get(url)
        data = response.json()
        
        image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/{pokemon_id}.gif"
        p = Pokemon(id=data['id'], name=data['name'], image_url=image_url)
        p.save()
        
        for pokemon_type in data['types']:
            t = Type.objects.get(name=pokemon_type['type']['name'])
            p.types.add(t)
        
        print(f"Added: {p}")
            
    print(f"{NO_OF_POKEMON} Pokemon added.")
    

def getTypes():
    pokemon_types = Type.objects.all()
    for pokemon_type in pokemon_types:
        print(pokemon_type)
        
def deleteAllTypes():
    types = Type.objects.all()
    for t in types:
        t.delete()
    print("Deleted all Pokemon Types in the Database")
        
def deleteAllPokemon():
    pk = Pokemon.objects.all()
    for p in pk:
        p.delete()
    print("Deleted all Pokemon in the Database")