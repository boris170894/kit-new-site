from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('', views.staff, name='staff'),
    path('<str:slug>', views.staff_one, name='staff_one' )
]
