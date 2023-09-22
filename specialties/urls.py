from django.urls import path
from . import views

app_name = 'spec'

urlpatterns = [
    path('', views.index, name='specialties'),
    path('<int:pk>', views.special, name='special'),
]