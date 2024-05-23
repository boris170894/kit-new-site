from django.shortcuts import render, get_object_or_404

from .models import (
                        CollegePartnersModel, 
                        CollegeSliderModel,
                        CollegeSliderImageModel,

                        IntroLogosModel,
                     )
from news.models import NewsModel

""" 
    TODO: Главная страница 
"""
def index(request):
    last_news = achivments = last_one_news = []
    public__news_count = NewsModel.objects.filter(news_is_published=True).count()
    intro_logos = IntroLogosModel.objects.filter(public=True).last()

    partners = CollegePartnersModel.objects.all()
    slides = CollegeSliderModel.objects.filter(public=True)
    print('SLIDES', slides)

    if public__news_count > 3:
        last_news = NewsModel.objects.filter(news_is_published = True).order_by('news_create_date')[public__news_count-4:public__news_count-1]        
        last_one_news = NewsModel.objects.filter(news_is_published = True).order_by('news_create_date')[public__news_count-1]

    achivments = NewsModel.objects.filter(news_is_published = True, news_is_achivment = True).order_by('-news_create_date')[:3]

    context = {
        'last_news': last_news,
        'partners': partners,
        'achivments': achivments,
        
        'last_one_news': last_one_news,
        'public__news_count': public__news_count,
        'slides': slides,
        'intro_logos': intro_logos,
    }
    return render(request, 'main/pages/index.html', context)


"""
    TODO: Кабинеты
"""
def slides(request):
    slides_all = CollegeSliderModel.objects.filter(public=True)

    context = {
        'slides': slides_all,
    }
    return render(request,'main/pages/index/slides.html', context)

"""
    TODO: Кабинет
"""
def slide(request, id):
    slider = CollegeSliderModel.objects.get(id=id)
    images = CollegeSliderImageModel.objects.filter(college_slider=slider, public=True)

    context = {
        'slider': slider,
        'images': images,
    }
    return render(request,'main/pages/index/slider.html', context)