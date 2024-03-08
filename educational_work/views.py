from django.shortcuts import render, redirect
from django.contrib import messages
from .models import  (GeneralInformationFilesModel, 
                                        ClubsAndSectionsModel, 
                                        ClubsAndSectionsDocumentsModel,
                                        PsychologicalServiceModel, 
                                        DormitoryModel)
from staff.models import (GroupModel)
from main.models import (SliderForDocumentListModel)

from django.core.mail import send_mail
from django.conf import settings


""" Общая информация """
def general_information(request):
    title = 'Общая информация'

    general_information_files = GeneralInformationFilesModel.objects.filter(is_public=True)
    slider = SliderForDocumentListModel.objects.filter(page=title).last()

    return render(request, 'about_college/counsil.html', {
        "title": title,
        "documents": general_information_files,
        "slider": slider,
    })

""" Кружки и секции """
def sections_and_circles(request):
    title = 'Кружки и секции'
    categories = ClubsAndSectionsModel.objects.all()
    documents = ClubsAndSectionsDocumentsModel.objects.filter(public=True)
    slider = SliderForDocumentListModel.objects.filter(page=title).last()

    return render(request, 'educational_work/sections.html', {
        'title': title,
        'categories': categories,
        'documents': documents,
        'slider': slider,
    })

""" Психологическая служба """
def psychological_service(request):
    title = 'Психологическая служба'
    documents = PsychologicalServiceModel.objects.filter(is_public=True).order_by('title')
    slider = SliderForDocumentListModel.objects.filter(page=title).last()

    return render(request, 'about_college/counsil.html', {
        'title': title,
        'documents': documents,
        'slider': slider,
    })

""" Общежитие """
def dormitory(request):
    info = DormitoryModel.objects.last()

    if request.method == 'POST':
        fio = request.POST.get('fio', '')
        group = request.POST.get('group', '')
        gender = request.POST.get('gender', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')

        subject = f"{fio} заявка на общежитие"
        body = f'{fio} - {group} - {gender} - {email} - {phone}'

        try: 
            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            messages.success(request, 'Email sent successfully!')            
            return redirect('/dormitory')
            
        except Exception as e:
            print('Error sending email', e)
            messages.error(request, "Connection error...")

    return render(request, 'educational_work/dormitory.html', {
        'info': info,
    })

""" Группы """
def groups(request):
    groups = GroupModel.objects.all()

    return render(request, 'educational_work/groups.html', {
        'groups': groups
    })