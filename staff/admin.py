from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin

from .models import (
                                GroupModel,
                                CMCModel,
                                PositionModel,
                                PersonModel
                            )


# """ CKEditor """
# class DirectorAdminForm(forms.ModelForm):
#     info_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Информация_[ru]')
#     info_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Информация_[kk]')

# @admin.register(DirectorModel)
# class DirectorAdmin(TranslationAdmin):
#     list_display = ('fio',)
#     prepopulated_fields = {'slug':('fio',)}
#     form = DirectorAdminForm

""" Группа """
@admin.register(GroupModel)
class GroupAdmin(TranslationAdmin):
    list_display = ('name', 'curator', )

""" ЦМК """
@admin.register(CMCModel)
class CMCAdmin(TranslationAdmin):
    list_display = ('title',)

""" Должность """
@admin.register(PositionModel)
class PositionAdmin(TranslationAdmin):
    list_display = ('title', 'cmc', )

class PersonAdminForm(forms.ModelForm):
    info_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[ru]')
    info_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[kk]')
    info_en = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[en]')
    class Meta:
        model = PersonModel
        fields = '__all__'

""" Персонал """
@admin.register(PersonModel)
class PersonAdmin(TranslationAdmin):
    prepopulated_fields = {'slug':('fio',)}
    list_display = ('fio', 'position', 'cmc')
    form = PersonAdminForm