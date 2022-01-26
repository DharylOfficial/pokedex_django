import pytest
from rest_framework import status
from rest_framework.test import APIClient

@pytest.mark.django_db
class TestPokemonCRUD:
    def test_if_pokemon_get_returns_200(self):
        client = APIClient()
        response = client.get('/api/pokemon/')
        assert response.status_code == status.HTTP_200_OK
        
    def test_if_pokemon_get_details_returns_200(self):
        client = APIClient()
        response = client.get('/api/pokemon/', {'id':1})
        assert response.status_code == status.HTTP_200_OK
        
    def test_if_pokemon_post_returns_201(self):
        client = APIClient()
        response = client.post('/api/pokemon/', {'name':'a'})
        assert response.status_code == status.HTTP_201_CREATED
        
    @pytest.mark.skip
    def test_if_pokemon_patch_returns_200(self):
        client = APIClient()
        response = client.patch('/api/pokemon/1', {'id':1,'name':'a'})
        assert response.status_code == status.HTTP_200_OK
        
    @pytest.mark.skip
    def test_if_pokemon_put_returns_200(self):
        client = APIClient()
        response = client.put('/api/pokemon/1', {'id':'1','name':'a'})
        assert response.status_code == status.HTTP_200_OK
    
    @pytest.mark.skip
    def test_if_pokemon_delete_returns_204(self):
        client = APIClient()
        response = client.delete('/api/pokemon/1',{'id': '1'})
        assert response.status_code == status.HTTP_204_NO_CONTENT