from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import (AntiCorruptionModel, 
                                    StateSymbolsModel,
                                    StateServicesModel,
                                    PolyiyasiaProgramModel)
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

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

@admin.register(StateSymbolsModel)
class StateSymbolsAdmin(TranslationAdmin):
    list_display = ('name', 'image', 'updated', )
    form = StateSymbolsAdminForm

@admin.register(StateServicesModel)
class StateServicesAdmin(TranslationAdmin):
    list_display = ('title', 'public', 'updated', 'file', )

@admin.register(PolyiyasiaProgramModel)
class PolyiyasiaProgramAdmin(TranslationAdmin):
    list_display = ('title', 'public', 'updated', 'file', )