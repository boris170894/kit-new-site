from django.shortcuts import render, get_object_or_404
from .models import SpecInfoModel


def index(request):
    type = 'many'
    specialites = SpecInfoModel.objects.all()
    
    return render(request, 'specialites/pages/about/specialites.html', {
        'type': type,
        'specialites': specialites
    })

def special(request, pk):
    type = 'one'
    spec= get_object_or_404(SpecInfoModel, pk=pk)
    
    return render(request, 'specialites/pages/about/specialites.html', {
        'type': type,
        'special': spec
    })
    