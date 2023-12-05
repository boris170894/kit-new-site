from django.shortcuts import render, get_object_or_404

from .models import (
                        CollegeContactModel, 
                        CollegePartnersModel, 
                        CollegeHistoryModel, 
                        CollegeDocsModel,
                        StateSymbolsModel,
                        CallPairScheduleModel,
                        AcademicProcessScheduleModel,
                        StudentEventModel,
                        MetodicRecomendationsCategoryModel,
                        MetodicRecomendationsDocumentModel,
                     )
from news.models import NewsModel
from specialties.models import SpecInfoModel


""" Главная страница  """
def index(request):
    last_news = achivments = last_one_news = []
    public__news_count = NewsModel.objects.filter(news_is_published = True).count()

    contacts = CollegeContactModel.objects.all()
    partners = CollegePartnersModel.objects.all()

    if public__news_count > 3:
        last_news = NewsModel.objects.filter(news_is_published = True).order_by('news_create_date')[public__news_count-4:public__news_count-1]        
        last_one_news = NewsModel.objects.filter(news_is_published = True).order_by('news_create_date')[public__news_count-1]

    achivments = NewsModel.objects.filter(news_is_published = True, news_is_achivment = True).order_by('-news_create_date')[:3]

    context = {
        'last_news': last_news,
        'contacts' : contacts,
        'partners' : partners,
        'achivments' : achivments,
        
        'last_one_news': last_one_news,
        'public__news_count': public__news_count,
    }
    return render(request, 'main/pages/index.html', context)

"""
        О колледже
"""

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

"""
        Государство
"""

""" Государственные Символы """
def state_symbols(request):
    symbols = StateSymbolsModel.objects.all()[:3]
    
    return render(request, 'main/pages/state/state_symbols.html', {
        'symbols': symbols
    })
    

"""
    TODO: Для студентов
"""
    
""" Расписание звонков и основное расписание для студентов """
def call_pair_schedule_students(request):
    docs  = CallPairScheduleModel.objects.last()
    
    return render(request, 'main/pages/information/student.html', {
        'type': 'Расписание пар и звонков',
        'user_type': 'student',
        'docs': docs
    })
    
""" График Учебного процесса для студентов """
def academic_process_schedule_students(request):
    docs  = AcademicProcessScheduleModel.objects.last()
    
    return render(request, 'main/pages/information/student.html', {
        'type': 'График учебного процесса',
        'user_type': 'student',
        'docs': docs
    })
    
""" Методические рекомендации для студентов """
def guidelines_students(request):
    
    return render(request, 'main/pages/information/student.html', {
        'type': 'Методические рекомендации',
        'user_type': 'student',
    })
    
""" События для студентов """
def student_events(request):
    events  = StudentEventModel.objects.all()
    
    return render(request, 'main/pages/information/student.html', {
        'type': 'События',
        'user_type': 'student',
        'events': events
    })

""" Показ одного события  для студентов """
def student_event_one(request, pk):
    event = get_object_or_404(StudentEventModel, pk=pk)
    
    return render(request, 'main/pages/information/student.html', {
        'type': event.title,
        'user_type': 'student',
        'event': event
    })
    
"""
    TODO: Для учителей
"""
    
""" Расписание звонков и основное расписание для учителей """
def call_pair_schedule_teachers(request):
    docs  = CallPairScheduleModel.objects.last()
    
    return render(request, 'main/pages/information/student.html', {
        'type': 'Расписание пар и звонков',
        'user_type': 'teacher',
        'docs': docs
    })
    
""" График Учебного процесса для учителей """
def academic_process_schedule_teachers(request):
    docs  = AcademicProcessScheduleModel.objects.last()
    
    return render(request, 'main/pages/information/student.html', {
        'type': 'График учебного процесса',
        'user_type': 'teacher',
        'docs': docs
    })
    
""" Методические рекомендации для учителей """
def guidelines_teachers(request):
    filter_title = request.GET.get('title', '')

    categories = MetodicRecomendationsCategoryModel.objects.filter(is_for_teacher=True)
    documents = MetodicRecomendationsDocumentModel.objects.all()

    if len(filter_title) > 0:
        documents = MetodicRecomendationsDocumentModel.objects.filter(title__icontains=filter_title)
    
    return render(request, 'main/pages/information/student.html', {
        'type': 'Методические рекомендации',
        'user_type': 'teacher',
        'categories': categories,
        'documents': documents,
        'filter_title': filter_title
    })
    