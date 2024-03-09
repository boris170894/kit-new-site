from django.shortcuts import render, get_object_or_404
from .models import (  CollegeHistoryModel, 
                                    CollegeDocsModel,
                                    BoardOfTrusteesModel,
                                    PedagogicalCouncilModel,
                                    IndustrialCouncilModel,
                                    SpecInfoModel,
                                    CollegeTextHistoryModel,
                                    GalleryModel
                        )
from main.models import SliderForDocumentListModel

"""
    TODO: ABOUT COLLEGE
"""

""" История Колледжа  """
def about_college_history(request):
    histories = CollegeHistoryModel.objects.filter(public=True).order_by('year')
    text = CollegeTextHistoryModel.objects.filter(public=True).first()
    
    return render(request, 'about_college/history.html', {
        'histories': histories,
        'text': text,
    })

""" Документы """
def about_documents(request):
    documents = CollegeDocsModel.objects.last()

    return render(request, 'about_college/documents.html', {
        'documents': documents
    })

""" Специальности """
def index(request):
    type = 'many'
    specialites = SpecInfoModel.objects.all()
    
    return render(request, 'about_college/specialites.html', {
        'type': type,
        'specialites': specialites
    })

def special(request, pk):
    type = 'one'
    spec= get_object_or_404(SpecInfoModel, pk=pk)
    
    return render(request, 'about_college/specialites.html', {
        'type': type,
        'special': spec
    })
    

""" Попечительский совет """
def about_board_of_trustees(request):
    title = 'Попечительский совет'
    documents = BoardOfTrusteesModel.objects.all().filter(public=True).order_by('title')
    slider = SliderForDocumentListModel.objects.filter(page=title).last()

    return render(request, 'about_college/counsil.html', {
        'title': title,
        'documents': documents,
        'slider': slider,
    })
    
""" Педагогический совет """
def about_pedagogical_council(request):
    title = 'Педагогический совет'
    documents = PedagogicalCouncilModel.objects.all().filter(public=True).order_by('title')
    slider = SliderForDocumentListModel.objects.filter(page=title).last()

    return render(request, 'about_college/counsil.html', {
        'title': title,
        'documents': documents,
        'slider': slider,
    })
    
""" Индустриальный совет """
def  about_industrial_council(request):
    title = 'Индустриальный совет'
    documents = IndustrialCouncilModel.objects.all().filter(public=True).order_by('title')
    slider = SliderForDocumentListModel.objects.filter(page=title).last()

    return render(request, 'about_college/counsil.html', {
        'title': title,
        'documents': documents,
        'slider': slider,
    })

""" Галерея """
def gallery(request):
    images = GalleryModel.objects.filter(public=True)

    return render(request, 'about_college/gallery.html', {
        'images': images,
    })
    