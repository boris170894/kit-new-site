from django.shortcuts import render
from .models import AntiCorruptionModel

def anti_corruption(request):
    last_file = AntiCorruptionModel.objects.all()[0]

    return render(request, 'state/anti_corruption.html', {
        "last_file": last_file
    })