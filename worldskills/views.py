from django.shortcuts import render
from django.core.paginator import Paginator

from .models import RuleWorldSkillsModel, CompetentionModel, CompetentionDocumentationModel
from news.models import NewsModel

def worldskills_rools(request):
    rules = []
    rules = RuleWorldSkillsModel.objects.all()

    if rules.count() > 0:
        rules = rules[0]

    return render(request, 'worldskills/rules.html', {
        'rules': rules
    })

def worldskills_competentions(request):
    categories = CompetentionModel.objects.all()
    documents = CompetentionDocumentationModel.objects.all()

    return render(request, 'worldskills/competentions.html', {
        'title': 'Документация к компетенциям',
        'categories': categories,
        'documents': documents,
    })

def show_all_worldskills_news(request):
    news_list = NewsModel.objects.filter(news_is_published = True, news_is_achivment=True).order_by('-news_create_date')    
    
    if request.method == 'GET':
        filters = request.GET.get('filters')
        
        if filters == 'oldest':
            news_list = NewsModel.objects.filter(news_is_published = True, news_is_worldskills=True).order_by('news_create_date') 
        else:
            news_list = NewsModel.objects.filter(news_is_published = True, news_is_achivment=True).order_by('-news_create_date')               
    
    paginator = Paginator(news_list, 8)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    return render(request, 'news/news_list.html', {
        'page': page,
        'type': "worldskills",
    })