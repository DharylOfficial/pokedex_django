from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    # pokemon_set
    
    def __str__(self) -> str:
        return f"{self.id}: {self.name}"
    
class Pokemon(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    types = models.ManyToManyField(Type)
    
    def __str__(self) -> str:
        return f"{self.id}: {self.name}"