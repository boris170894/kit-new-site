from django.shortcuts import render
from .models import (
                        AnnouncementVacanciesModel,
                        AnnouncementModel,
                        AnnouncementFilesModel,
                        AnnouncementImagesModel,
                    )


""" Объявления """
def announcement(request):
    info = AnnouncementModel.objects.filter(is_public=True).last()
    vacancies = AnnouncementVacanciesModel.objects.filter(is_public=True)
    files = AnnouncementFilesModel.objects.filter(is_public=True)
    images = AnnouncementImagesModel.objects.filter(is_public=True)

    return render(request, 'announcements/announcements.html', {
        "info": info,
        'vacancies': vacancies,
        'files': files,
        'images': images,
    })