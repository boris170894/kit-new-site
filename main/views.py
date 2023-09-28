from django.shortcuts import render, get_object_or_404

from .models import (
                        CollegeContactModel, 
                        CollegePartnersModel, 
                        CollegeHistoryModel, 
                        CollegeDocsModel,
                        StateSymbolsModel,
                        CallPairScheduleModel,
                        AcademicProcessScheduleModel,
                        StudentEventModel
                     )
from news.models import NewsModel
from specialties.models import SpecInfoModel


""" Главная страница  """
def index(request):
    public__news_count = NewsModel.objects.filter(news_is_published = True).count()
    last_news = NewsModel.objects.filter(news_is_published = True).order_by('news_create_date')[public__news_count-4:public__news_count-1]
    achivments = NewsModel.objects.filter(news_is_published = True, news_is_achivment = True).order_by('-news_create_date')[:3]
    
    contacts = CollegeContactModel.objects.all()
    partners = CollegePartnersModel.objects.all()
    
    last_one_news = NewsModel.objects.filter(news_is_published = True).order_by('news_create_date')[public__news_count-1]

    context = {
        'last_news': last_news,
        'contacts' : contacts,
        'partners' : partners,
        'achivments' : achivments,
        
        'last_one_news': last_one_news,
    }
    return render(request, 'main/pages/index.html', context)

""" Абитуриенты  """
def abiturients(request):
    
    specs = SpecInfoModel.objects.all()
    contacts = CollegeContactModel.objects.all()

    return render(request, 'main/pages/information/abiturients.html', {
        'specialites' : specs,
        'contacts' : contacts,
    })

""" История Колледжа  """
def college_history(request):
    histories = CollegeHistoryModel.objects.all().order_by('year')
    
    return render(request, 'main/pages/about/history.html', {
        'histories': histories
    })

""" Документы """
def documents(request):
    documents = CollegeDocsModel.objects.last()

    return render(request, 'main/pages/about/documents.html', {
        'documents': documents
    })

""" Государственные Символы """
def state_symbols(request):
    symbols = StateSymbolsModel.objects.all()[:3]
    
    return render(request, 'main/pages/state/state_symbols.html', {
        'symbols': symbols
    })
    
""" Расписание звонков и основное расписание """
def call_pair_schedule(request):
    docs  = CallPairScheduleModel.objects.last()
    
    return render(request, 'main/pages/information/student.html', {
        'type': 'Расписание пар и звонков',
        'docs': docs
    })
    
""" График Учебного процесса """
def academic_process_schedule(request):
    docs  = AcademicProcessScheduleModel.objects.last()
    
    return render(request, 'main/pages/information/student.html', {
        'type': 'График учебного процесса',
        'docs': docs
    })
    
""" Методические рекомендации """
def guidelines_students(request):
    
    return render(request, 'main/pages/information/student.html', {
        'type': 'Методические рекомендации',
    })
    
""" События для студентов """
def student_events(request):
    events  = StudentEventModel.objects.all()
    
    return render(request, 'main/pages/information/student.html', {
        'type': 'События',
        'events': events
    })

""" Событие  для студентов """
def student_event_one(request, pk):
    event = get_object_or_404(StudentEventModel, pk=pk)
    
    return render(request, 'main/pages/information/student.html', {
        'type': event.title,
        'event': event
    })