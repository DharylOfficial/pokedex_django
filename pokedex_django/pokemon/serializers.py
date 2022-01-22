from rest_framework import serializers
from .models import Type, Pokemon

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ["id", "name"]

class PokemonSerializer(serializers.ModelSerializer):
    type_details = TypeSerializer(read_only=True, many=True, source='types')
    
    # TO UPDATE TYPES, ONLY LIST TYPE IDs ARE NEEDED
    class Meta:
        model = Pokemon
        fields = ["id", "name", "image_url", "types", "type_details"]