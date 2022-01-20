from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    # pokemon_set
    
class Pokemon(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    types = models.ManyToManyField(Type)
    
# class PokemonType(models.Model):
#     pokemon = models.ForeignKey(Pokemon, null=True, blank=True, on_delete=models.DO_NOTHING)
#     type = models.ForeignKey(Type, null=True, blank=True, on_delete=models.DO_NOTHING)