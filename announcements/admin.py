from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import (
                        AnnouncementVacanciesModel,
                        AnnouncementModel,
                        AnnouncementFilesModel,
                        AnnouncementImagesModel,
                    )


class AnnouncementAdminForm(forms.ModelForm):
    about_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание [ru]')
    about_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание [kk]')
    about_en = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание [en]')

    class Meta:
        model = AnnouncementModel
        fields = '__all__'

""" Объявления """
@admin.register(AnnouncementModel)
class AnnouncementAdmin(TranslationAdmin):
    list_display = ('id', 'updated', )
    form = AnnouncementAdminForm

""" Объявления, Загрузка файлов """
@admin.register(AnnouncementFilesModel)
class AnnouncementFilesAdmin(TranslationAdmin):
    list_display = ('title', 'is_public', 'updated', )

""" Объявления, Загрузка фото """
@admin.register(AnnouncementImagesModel)
class AnnouncementImagesAdmin(TranslationAdmin):
    list_display = ('id', 'file', 'is_public', 'updated', )

class AnnouncementVacanciesAdminForm(forms.ModelForm):
    description_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание [ru]')
    description_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание [kk]')
    description_en = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание [en]')

    class Meta:
        model = AnnouncementVacanciesModel
        fields = '__all__'

""" Объявления, Вакансии """
@admin.register(AnnouncementVacanciesModel)
class AnnouncementVacanciesAdmin(TranslationAdmin):
    list_display = ('title', 'updated')
    form = AnnouncementVacanciesAdminForm