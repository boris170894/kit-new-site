from django.shortcuts import render
from .models import (AntiCorruptionModel,
                                    StateSymbolsModel,
                                    StateServicesModel,
                                    PolyiyasiaProgramModel,
                                    )

"""
    TODO:    Государство
"""

""" Государственные Символы """
def state_symbols(request):
    symbols = StateSymbolsModel.objects.all()[:3]
    
    return render(request, 'main/pages/state/state_symbols.html', {
        'symbols': symbols,
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
    documents = AntiCorruptionModel.objects.filter(public=True)

    return render(request, 'about_college/counsil.html', {
        'title': 'Противодействие коррупции',
        "documents": documents,
    })

""" Программа полиязычия """
def polyiyasia_program(request):
    documents = PolyiyasiaProgramModel.objects.filter(public=True)

    return render(request, 'about_college/counsil.html', {
        'title': 'Программа полиязычия',
        'documents': documents,
    })