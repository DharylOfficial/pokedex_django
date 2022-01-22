from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('pull', views.pullAll, name="pullAll"),
    path('pull/types', views.pullTypes, name="pullTypes"),
    path('pull/pokemon', views.pullPokemon, name="pullPokemon"),
    path('get/types', views.getTypes, name="pullTypes"),
    
    path('test_type_normal', views.test_type_normal, name="test_type_normal"),
]