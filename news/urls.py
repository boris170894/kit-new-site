from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>/", views.NewsView.as_view(), name = 'news_view'),
    path("", views.NewsListView.as_view(), name='news_list'),
]
