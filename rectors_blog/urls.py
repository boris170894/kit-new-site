from django.urls import path, include
from . import views

urlpatterns = [
    path('greeting/', views.greeting, name='greeting'),
    path('questions/', views.questions, name='questions'),
]