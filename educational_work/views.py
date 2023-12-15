from django.shortcuts import render
from .models import GeneralInformationFilesModel

def general_information(request):
    general_information_files = GeneralInformationFilesModel.objects.all()

    return  render(request, 'educational_work/general_information.html', {
        "documents": general_information_files, 
    })