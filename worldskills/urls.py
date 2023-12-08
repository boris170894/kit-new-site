from django.urls import path
from . import views

urlpatterns = [
    path('rools/', views.worldskills_rools, name='worldskills-rools'),
    path('documents/', views.worldskills_competentions, name='worldskills-competentions'),
    path('news/', views.show_all_worldskills_news, name='show-all-worldskills-news'),
]