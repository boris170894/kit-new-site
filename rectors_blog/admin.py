from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import RectorsBlogMainInfoModel, RectorsBlogQuestionAnswerModel
from django.forms import CharField, ModelForm

class RectorsBlogMainInfoAdminForm(ModelForm):
    info_ru = CharField(widget=CKEditorUploadingWidget(), label='Приветсвие [ru]')
    info_kk = CharField(widget=CKEditorUploadingWidget(), label='Приветсвие [kk]')
    info_en = CharField(widget=CKEditorUploadingWidget(), label='Приветсвие [en]')

    class Meta:
        model = RectorsBlogMainInfoModel
        fields = '__all__'

""" Блог Ректора Главная информация """
@admin.register(RectorsBlogMainInfoModel)
class RectorsBlogMainInfoAdmin(TranslationAdmin):
    list_display = ('fio', 'updated', )
    form = RectorsBlogMainInfoAdminForm

""" Блог Ректора Вопрос - Ответ """
@admin.register(RectorsBlogQuestionAnswerModel)
class RectorsBlogQuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'email', 'created', 'updated',)
