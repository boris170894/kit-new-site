from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import (AntiCorruptionModel,
                        PresidentialMessageModel,
                        StateSymbolsModel,
                        StateServicesModel,
                        PolyiyasiaProgramModel)
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

""" Противодействие коррупции """
@admin.register(AntiCorruptionModel)
class AntiCorruptionsAdmin(TranslationAdmin):
    list_display = ('title', 'public', 'file', )

class StateSymbolsAdminForm(forms.ModelForm):
    desc_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[ru]')
    desc_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[kk]')
    desc_en = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[en]')
    
    class Meta:
        model = StateSymbolsModel
        fields = '__all__'

""" Государственные Символы """
@admin.register(StateSymbolsModel)
class StateSymbolsAdmin(TranslationAdmin):
    list_display = ('name', 'image', 'updated', )
    form = StateSymbolsAdminForm

class PresidentialMessageAdminForm(forms.ModelForm):
    text_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[ru]')
    text_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[kk]')
    text_en = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[en]')

    class Meta:
        model = StateSymbolsModel
        fields = '__all__'

""" Послание президента """
@admin.register(PresidentialMessageModel)
class PresidentialMessageAdmin(TranslationAdmin):
    list_display = ('title', 'updated', 'is_public', )
    form = PresidentialMessageAdminForm

@admin.register(StateServicesModel)
class StateServicesAdmin(TranslationAdmin):
    list_display = ('title', 'public', 'updated', 'file', )

@admin.register(PolyiyasiaProgramModel)
class PolyiyasiaProgramAdmin(TranslationAdmin):
    list_display = ('title', 'public', 'updated', 'file', )