from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.core.paginator import Paginator

from .models import NewsModel

def show_all_news(request):
    news_list = NewsModel.objects.filter(news_is_published=True).order_by('-news_create_date')    
    
    if request.method == 'GET':
        filters = request.GET.get('filters')
        
        if filters == 'oldest':
            news_list = NewsModel.objects.filter(news_is_published=True).order_by('news_create_date') 
        else:
            news_list = NewsModel.objects.filter(news_is_published=True).order_by('-news_create_date')               
    
    paginator = Paginator(news_list, 8)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    return render(request, 'news/news_list.html', {
        'page': page
    })

def show_about_world_skills(request):
    worldskillses = NewsModel.objects.filter(news_is_published = True).order_by('-news_create_date')    

    return render(request, 'news/news_list.html', {
        # 'page': page
    })

def show_one_news(request, slug):
    news = NewsModel.objects.get(slug=slug)
    
    return render(request, 'news/news.html', {
        'news':news
    })
    