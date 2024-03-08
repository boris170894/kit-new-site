from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name ='index'),

    path('slides/', views.slides, name='slides'),
    path('slides/<int:id>', views.slide, name='slide'),
]
