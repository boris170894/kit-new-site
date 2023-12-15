from django.shortcuts import render, get_object_or_404
from .models import (  CollegeHistoryModel, 
                                    CollegeDocsModel,
                                    BoardOfTrusteesModel,
                                    PedagogicalCouncilModel,
                                    IndustrialCouncilModel  )

"""
    TODO: ABOUT COLLEGE
"""

""" История Колледжа  """
def about_college_history(request):
    histories = CollegeHistoryModel.objects.all().order_by('year')
    
    return render(request, 'about_college/history.html', {
        'histories': histories
    })

""" Документы """
def about_documents(request):
    documents = CollegeDocsModel.objects.last()

    return render(request, 'about_college/documents.html', {
        'documents': documents
    })

""" Попечительский совет """
def about_board_of_trustees(request):
    documents = BoardOfTrusteesModel.objects.all().filter(public=True).order_by('title')

    return render(request, 'about_college/counsil.html', {
        'title': 'Попечительский совет',
        'documents': documents
    })
    
""" Педагогический совет """
def about_pedagogical_council(request):
    documents = PedagogicalCouncilModel.objects.all().filter(public=True).order_by('title')

    return render(request, 'about_college/counsil.html', {
        'title': 'Педагогический совет ',
        'documents': documents
    })
    
""" Индустриальный совет """
def  about_industrial_council(request):
    documents = IndustrialCouncilModel.objects.all().filter(public=True).order_by('title')

    return render(request, 'about_college/counsil.html', {
        'title': 'Индустриальный совет ',
        'documents': documents
    })
    