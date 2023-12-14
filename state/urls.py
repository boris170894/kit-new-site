from django.urls import path
from . import views

urlpatterns = [
    path("anti-corruption", views.anti_corruption, name="anti-corruption"),
]
