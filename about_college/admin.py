from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import (CollegeHistoryModel,
                                    CollegeDocsModel,
                                    SpecInfoModel, 
                                    BoardOfTrusteesModel,
                                    PedagogicalCouncilModel,
                                    IndustrialCouncilModel )

class CollegeHistoryAdminForm(forms.ModelForm):
    info_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[ru]')
    info_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[kk]')
    info_en = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[en]')
    class Meta:
        model = CollegeHistoryModel
        fields = '__all__'

""" История колледжа """
@admin.register(CollegeHistoryModel)
class CollegeHistoryAdmin(TranslationAdmin):
    list_display = ('year',)
    form = CollegeHistoryAdminForm

""" Документы """
admin.site.register(CollegeDocsModel)

class SpecAdminForm(forms.ModelForm):
    spec_info_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[ru]')
    spec_info_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[kk]')
    spec_info_en = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[en]')
    class Meta:
        model = SpecInfoModel
        fields = '__all__'

""" Специальности """
@admin.register(SpecInfoModel)
class SpecInfoAdmin(TranslationAdmin):
    list_display = ('spec_name',)
    form = SpecAdminForm

""" Попечительский совет """
@admin.register(BoardOfTrusteesModel)
class BoardOfTrusteesAdmin(TranslationAdmin):
    list_display = ('title', 'file', 'public', )

""" Педагогический совет """
@admin.register(PedagogicalCouncilModel)
class PedagogicalCouncilAdmin(TranslationAdmin):
    list_display = ('title', 'file', 'public', )

""" Индустриальный совет """
@admin.register(IndustrialCouncilModel)
class IndustrialCouncilAdmin(TranslationAdmin):
    list_display = ('title', 'file', 'public', )