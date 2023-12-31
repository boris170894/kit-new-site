from django.urls import path
from . import views


urlpatterns = [
    path("", views.show_all_news, name='news_list'),
    path("<slug:slug>/", views.show_one_news, name = 'show_one_news'),
]
