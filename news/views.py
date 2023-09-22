from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from .models import NewsModel

class NewsView(View):

    def get(self, request, slug):
        news_view = NewsModel.objects.get(slug = slug)
        return render(request, 'news/news.html', {'news_view':news_view})
    

class NewsListView(View):

    def get(self, request):
        news_list = NewsModel.objects.filter(news_is_published = True).order_by('-news_create_date')
        return render(request, 'news/news_list.html', {'news_list': news_list})
