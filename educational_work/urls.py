from django.urls import path
from . import views

urlpatterns = [
    path('general-information/', views.general_information, name='general-information'),
    path('sections/', views.sections_and_circles, name='sections-and-circles'),
    path('psychological-service/', views.psychological_service, name='psychological-service'),
    path('groups/', views.groups, name='groups'),
    path('youth-policy/', views.youth_policy, name='youth-policy'),
    path('antiterror/', views.terror, name="antiterror"),
]
