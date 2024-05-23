from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from about_college.models import SpecInfoModel
from .models import (
                         CallPairScheduleModel,
                        AcademicProcessScheduleModel, StudentEventModel,
                        MetodicRecomendationsCategoryModel,  MetodicRecomendationsDocumentModel,
                        FinancialStatementsModel, 
                        CollegeDocsModel, MainAdvantagesOfOurCollegeModel,
                        LibraryModel, LibraryFilesModel, LibrarySliderImageModel,
                        DormitoryModel, DormitoryImagesModel, DormitoryFilesModel,
                        OurUnionModel, OurUnionFilesModel, OurUnionImagesModel
                     )
from news.models import NewsModel
from contacts.models import CollegeContactModel

"""
    TODO:    Абитуриенту
"""

""" Абитуриенты  """
def abiturients(request):
    specs = SpecInfoModel.objects.all()
    contacts = CollegeContactModel.objects.filter(public=True).last()
    docs = CollegeDocsModel.objects.filter(is_public=True)
    pluses = MainAdvantagesOfOurCollegeModel.objects.filter(is_public=True)

    return render(request, 'main/pages/information/abiturients.html', {
        'specialites': specs,
        'contacts': contacts,
        'docs': docs,
        'pluses': pluses
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
    images = LibrarySliderImageModel.objects.filter(is_public=True)
    files = LibraryFilesModel.objects.filter(is_public=True)

    paginator = Paginator(news_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'information/library.html', {
        'library': documents,
        'page': page,
        'documents': files,
        'images': images,
    })


""" Общежитие """
def dormitory(request):
    info = DormitoryModel.objects.filter(is_public=True).last()
    title = "Общежитие"
    images = DormitoryImagesModel.objects.filter(is_public=True)
    files = DormitoryFilesModel.objects.filter(is_public=True)

    if request.method == 'POST':
        fio = request.POST.get('fio', '')
        group = request.POST.get('group', '')
        gender = request.POST.get('gender', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')

        subject = f"{fio} заявка на общежитие"
        body = f'{fio} - {group} - {gender} - {email} - {phone}'

        # try:
        #     send_mail(
        #         subject,
        #         body,
        #         settings.EMAIL_HOST_USER,
        #         [settings.EMAIL_HOST_USER],
        #         fail_silently=False,
        #     )
        #
        #     messages.success(request, 'Email sent successfully!')
        #     return redirect('/dormitory')
        #
        # except Exception as e:
        #     print('Error sending email', e)
        #     messages.error(request, "Connection error...")

    return render(request, 'educational_work/dormitory.html', {
        'title': title,
        'info': info,
        'documents': files,
        'images': images,
    })

""" Наш профсоюз """
def our_union(request):
    title = "Наш профсоюз"
    info = OurUnionModel.objects.filter(is_public=True).last()
    images = OurUnionImagesModel.objects.filter(is_public=True)
    files = OurUnionFilesModel.objects.filter(is_public=True)

    return render(request, 'educational_work/dormitory.html', {
        'title': title,
        'info': info,
        'documents': files,
        'images': images,
    })