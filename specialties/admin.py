from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin
from django import forms

from .models import SpecInfoModel


class SpecInfoForm(forms.ModelForm):

    spec_info_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание_[ru]')
    spec_info_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание_[kk]')
    class Meta:
        model = SpecInfoModel
        fields = '__all__'

@admin.register(SpecInfoModel)
class SpecInfoAdmin(TranslationAdmin):
    form = SpecInfoForm

    list_display = ('spec_name',)