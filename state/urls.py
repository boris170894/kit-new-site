from django.urls import path
from . import views

urlpatterns = [
    path('state-symbols/', views.state_symbols, name = 'state-symbols'), 
    path('government-services/', views.state_services, name = 'state-services'), 
    path("anti-corruption", views.anti_corruption, name="anti-corruption"),
    path('multilingualism-program/', views.polyiyasia_program, name = 'polyiyasia-program'), 
]
