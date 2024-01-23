from django.shortcuts import render, redirect
from django.contrib import messages
from .models import  (GeneralInformationFilesModel, 
                                        ClubsAndSectionsModel, 
                                        ClubsAndSectionsDocumentsModel,
                                        PsychologicalServiceModel, 
                                        DormitoryModel)
from staff.models import (GroupModel)

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.conf import settings
import smtplib
from email.mime.text import MIMEText


""" Общая информация """
def general_information(request):
    general_information_files = GeneralInformationFilesModel.objects.filter(is_public=True)

    return  render(request, 'about_college/counsil.html', {
        "title": 'Общая информация',
        "documents": general_information_files, 
    })

""" Кружки и секции """
def sections_and_circles(request):
    categories = ClubsAndSectionsModel.objects.all()
    documents = ClubsAndSectionsDocumentsModel.objects.filter(public=True)

    return render(request, 'educational_work/sections.html', {
        'title': 'Кружки и секции ',
        'categories': categories,
        'documents': documents,
    })

""" Психологическая служба """
def psychological_service(request):
    documents = PsychologicalServiceModel.objects.filter(is_public=True).order_by('title')

    return render(request, 'about_college/counsil.html', {
        'title': 'Психологическая служба ',
        'documents': documents
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

            # msg = MIMEText(body)
            # msg['Subject'] = subject
            # msg['From'] = settings.EMAIL_HOST_USER
            # msg['To'] = ', '.join(settings.EMAIL_RECIPIENTS)
            # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            #     smtp_server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            #     smtp_server.sendmail(settings.EMAIL_HOST_USER, settings.EMAIL_RECIPIENTS, msg.as_string())
            #     print("Message sent!")

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