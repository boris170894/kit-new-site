from django.shortcuts import render
from .models import (AntiCorruptionModel,
                        StateSymbolsModel,
                        StateServicesModel,
                        PolyiyasiaProgramModel,
                        PresidentialMessageModel )
from main.models import SliderForDocumentListModel

"""
    TODO:    Государство
"""

""" Государственные Символы """
def state_symbols(request):
    symbols = StateSymbolsModel.objects.all()[:3]

    return render(request, 'main/pages/state/state_symbols.html', {
        'symbols': symbols,
    })

""" Послание президента (список) """
def presidential_message_list(request):
    type = 'Presidential Messages'
    message = PresidentialMessageModel.objects.filter(is_public=True).last()
    messages = PresidentialMessageModel.objects.filter(is_public=True).order_by('-created')

    return render(request, 'main/pages/state/state_symbols.html', {
        'presidential_message': message,
        'presidential_messages': messages,
        'page_type': type,
    })

""" Послание президента (одно) """
def presidential_message(request, id):
    type = 'Presidential Message'
    message = PresidentialMessageModel.objects.get(id=id)

    return render(request, 'main/pages/state/state_symbols.html', {
        'presidential_message': message,
        'page_type': type,
    })
    
""" Государственные услуги """
def state_services(request):
    documents = StateServicesModel.objects.filter(public=True)

    return render(request, 'about_college/counsil.html', {
        'title': 'Государственные услуги',
        'documents': documents,
    })

""" Противодействие коррупции """
def anti_corruption(request):
    title = 'Противодействие коррупции'

    documents = AntiCorruptionModel.objects.filter(public=True)
    slider = SliderForDocumentListModel.objects.filter(page=title).last()

    return render(request, 'about_college/counsil.html', {
        'title': title,
        'documents': documents,
        'slider': slider,
    })

""" Программа полиязычия """
def polyiyasia_program(request):
    title = 'Программа полиязычия'
    documents = PolyiyasiaProgramModel.objects.filter(public=True)
    slider = SliderForDocumentListModel.objects.filter(page=title).last()

    return render(request, 'about_college/counsil.html', {
        'title': title,
        'documents': documents,
        'slider': slider,
    })