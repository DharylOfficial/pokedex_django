from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

router  = routers.DefaultRouter()
router.register("type", views.TypeViewSet, basename="type")
router.register("pokemon", views.PokemonViewSet, basename="pokemon")

urlpatterns = [
    path("", include(router.urls)),
    path("reset/", views.resetPokedexEndpoint, name="resetPokedex")
]