from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin

from .models import *


""" CKEditor """
class DirectorAdminForm(forms.ModelForm):
    info_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Информация_[ru]')
    info_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Информация_[kk]')

    class Meta:
        model = DirectorModel
        fields = '__all__'

class DepDirectorAdminForm(forms.ModelForm):
    info_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Информация_[ru]')
    info_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Информация_[kk]')

    class Meta:
        model = DepDirectorModel
        fields = '__all__'   

class DepHeadAdminForm(forms.ModelForm):
    info_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Информация_[ru]')
    info_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Информация_[kk]')

    class Meta:
        model = DepHeadModel
        fields = '__all__'   

class DepHeadAdminForm(forms.ModelForm):
    info_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Информация_[ru]')
    info_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Информация_[kk]')

    class Meta:
        model = DepHeadModel
        fields = '__all__' 

class CmcOBAdminForm(forms.ModelForm):
    info_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Информация_[ru]')
    info_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Информация_[kk]')

    class Meta:
        model = CmcOBModel
        fields = '__all__'    

class CmcLangAdminForm(forms.ModelForm):
    info_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Информация_[ru]')
    info_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Информация_[kk]')

    class Meta:
        model = CmcLangModel
        fields = '__all__'   

class CmcELAdminForm(forms.ModelForm):
    info_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Информация_[ru]')
    info_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Информация_[kk]')

    class Meta:
        model = CmcELModel
        fields = '__all__'    

class CmcITAdminForm(forms.ModelForm):
    info_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Информация_[ru]')
    info_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Информация_[kk]')

    class Meta:
        model = CmcITModel
        fields = '__all__'   
 
class CmcFIZAdminForm(forms.ModelForm):
    info_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Информация_[ru]')
    info_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Информация_[kk]')

    class Meta:
        model = CmcFIZModel
        fields = '__all__'   

""" Регистрация моделей в админке """
@admin.register(PositionModel)
class PositionAdmin(TranslationAdmin):
    list_display = ('position_name',)


@admin.register(DirectorModel)
class DirectorAdmin(TranslationAdmin):
    list_display = ('fio',)
    prepopulated_fields = {'slug':('fio',)}
    form = DirectorAdminForm

@admin.register(DepDirectorModel)
class DepDirectorAdmin(TranslationAdmin):
    list_display = ('fio',)
    prepopulated_fields = {'slug':('fio',)}
    form = DepDirectorAdminForm


@admin.register(DepHeadModel)
class DepHeadAdmin(TranslationAdmin):
    list_display = ('fio',)
    prepopulated_fields = {'slug':('fio',)}
    form = DepHeadAdminForm

@admin.register(CmcOBModel)
class CmcOBAdmin(TranslationAdmin):
    list_display = ('fio',)
    prepopulated_fields = {'slug':('fio',)}
    form = CmcOBAdminForm

@admin.register(CmcLangModel)
class CmcLangAdmin(TranslationAdmin):
    list_display = ('fio',)
    prepopulated_fields = {'slug':('fio',)}
    form = CmcLangAdminForm


@admin.register(CmcELModel)
class CmcELAdmin(TranslationAdmin):
    list_display = ('fio',)
    prepopulated_fields = {'slug':('fio',)}
    form = CmcELAdminForm

@admin.register(CmcITModel)
class CmcITAdmin(TranslationAdmin):
    list_display = ('fio',)
    prepopulated_fields = {'slug':('fio',)}  
    form = CmcITAdminForm

@admin.register(CmcFIZModel)
class CmcFIZAdmin(TranslationAdmin):
    list_display = ('fio',)
    prepopulated_fields = {'slug':('fio',)}
    form = CmcFIZAdminForm