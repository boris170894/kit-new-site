from django.shortcuts import render, redirect
from django.contrib import messages
from .models import (GeneralInformationFilesModel,
                        ClubsAndSectionsModel, ClubsAndSectionsDocumentsModel,
                        PsychologicalServiceModel,
                        YouthPolicyModel,
                        )
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

""" Группы """
def groups(request):
    groups = GroupModel.objects.all()

    return render(request, 'educational_work/groups.html', {
        'groups': groups
    })

""" Молодежная политика """
def youth_policy(request):
    title = "Молодежная политика"
    info = YouthPolicyModel.objects.filter(is_public=True).last()

    return render(request, 'educational_work/dormitory.html', {
        'title': title,
        'info': info,
    })