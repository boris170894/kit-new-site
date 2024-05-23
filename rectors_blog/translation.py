from modeltranslation.translator import register, TranslationOptions
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import (
                        RectorsBlogMainInfoModel,
                        RectorsBlogQuestionAnswerModel,
                    )

class RectorsBlogMainInfoAdminForm(forms.ModelForm):
    info_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[ru]')
    info_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[kk]')
    info_en = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[en]')

    class Meta:
        model = RectorsBlogMainInfoModel
        fields = '__all__'

""" Блог Ректора Главная информация """
@register(RectorsBlogMainInfoModel)
class RectorsBlogMainInfoTransOptions(TranslationOptions):
    fields = ('fio', 'info', 'appointment_schedule', 'cabinet', )
    form = RectorsBlogMainInfoAdminForm

# """ Блог Ректора Вопрос - Ответ """
# @register(RectorsBlogQuestionAnswerModel)
# class RectorsBlogQuestionAnswerTransOptions(TranslationOptions):
#     fields = ('firstName', 'lastName', 'question', 'answer',)