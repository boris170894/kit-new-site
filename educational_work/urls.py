from django.urls import path
from . import views

urlpatterns = [
    path('general-information/', views.general_information, name='general-information'),
]
