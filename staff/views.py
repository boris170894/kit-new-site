from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.http import Http404

from .models import (
    DirectorModel,
    DepDirectorModel,
    DepHeadModel,
    CmcOBModel,
    CmcLangModel,
    CmcELModel,
    CmcITModel,
    CmcFIZModel
)


def staff(request):
    directors = DirectorModel.objects.filter(is_working=True)
    depDirectors = DepDirectorModel.objects.filter(is_working=True)
    depHead = DepHeadModel.objects.filter(is_working=True)
    cmsOB = CmcOBModel.objects.filter(is_working=True)
    cmsLang = CmcLangModel.objects.filter(is_working=True)
    cmsEL = CmcELModel.objects.filter(is_working=True)
    cmsIT = CmcITModel.objects.filter(is_working=True)
    cmsFIZ = CmcFIZModel.objects.filter(is_working=True)
    
    
    context = {
        'directors': directors,
        'depDirectors': depDirectors,
        'depHead': depHead,
        'cmsOB': cmsOB,
        'cmsLang': cmsLang,
        'cmsEl': cmsEL,
        'cmsIT': cmsIT,
        'cmsFIZ': cmsFIZ,
        
    }
    return render(request, 'staff/staff.html', context)

""" Show one """
def staff_one(request, slug):
    models_to_search = [DirectorModel,DepDirectorModel, DepHeadModel,CmcOBModel, CmcLangModel, CmcELModel, CmcITModel, CmcFIZModel ]
    
    obj = None
    
    for model_class in models_to_search:
        try:
            obj = model_class.objects.get(slug=slug)
            break
        except model_class.DoesNotExist:
            continue 
    
    if obj:
        return render(request, 'staff/object.html', {
            'person': obj
        })
    else:
        Http404
    