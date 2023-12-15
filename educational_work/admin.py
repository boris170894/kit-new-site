from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import GeneralInformationFilesModel

@admin.register(GeneralInformationFilesModel)
class GeneralInformationFilesAdmin(TranslationAdmin):
    list_display = ('title', 'updated_at', )