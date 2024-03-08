from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from about_college.models import SpecInfoModel
from .models import (
                        CollegeContactModel, 
                        CallPairScheduleModel,
                        AcademicProcessScheduleModel,
                        StudentEventModel,
                        MetodicRecomendationsCategoryModel,
                        MetodicRecomendationsDocumentModel,
                        FinancialStatementsModel, 
                        CollegeDocsModel,
                        MainAdvantagesOfOurCollegeModel,
                        LibraryModel,
                     )
from news.models import NewsModel

"""
    TODO:    Абитуриенту
"""

""" Абитуриенты  """
def abiturients(request):
    
    specs = SpecInfoModel.objects.all()
    contacts = CollegeContactModel.objects.all()
    docs = CollegeDocsModel.objects.filter(is_public=True)
    pluses = MainAdvantagesOfOurCollegeModel.objects.filter(is_public=True)

    return render(request, 'main/pages/information/abiturients.html', {
        'specialites' : specs,
        'contacts' : contacts,
        'docs': docs,
        'pluses' : pluses
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

""" Финансовая отчетность  """
def financial_statement(request):
    documents = FinancialStatementsModel.objects.filter(is_public=True).order_by('title')

    return render(request, 'about_college/counsil.html', {
        'title': 'Финансовая отчетность',
        'documents': documents
    })

""" Библиотека """
def library(request):
    documents = LibraryModel.objects.filter(is_public=True).last()
    news_list = NewsModel.objects.filter(news_is_library=True).filter(news_is_published=True).order_by('-news_create_date')

    paginator = Paginator(news_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'information/library.html', {
        'library': documents,
        'page': page
    })