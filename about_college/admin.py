from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import (CollegeHistoryModel,
                        CollegeDocsModel,
                        SpecInfoModel,
                        BoardOfTrusteesModel,
                        PedagogicalCouncilModel,
                        IndustrialCouncilModel,
                        CollegeTextHistoryModel,
                        GalleryModel
                     )

class CollegeHistoryAdminForm(forms.ModelForm):
    info_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[ru]')
    info_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[kk]')
    info_en = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[en]')
    class Meta:
        model = CollegeHistoryModel
        fields = '__all__'

""" История колледжа события """
@admin.register(CollegeHistoryModel)
class CollegeHistoryAdmin(TranslationAdmin):
    list_display = ('year', 'public',)
    form = CollegeHistoryAdminForm

class CollegeTextHistoryAdminForm(forms.ModelForm):
    text_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание [ru]')
    text_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание [kk]')
    text_en = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание [en]')

    our_mission_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Наша Миссия [ru]')
    our_mission_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Наша Миссия [kk]')
    our_mission_en = forms.CharField(widget=CKEditorUploadingWidget(), label='Наша Миссия [en]')

    class Meta:
        model = CollegeTextHistoryModel
        fields = '__all__'

""" История колледжа текст """
@admin.register(CollegeTextHistoryModel)
class CollegeTextHistoryAdmin(TranslationAdmin):
    list_display = ('updated', 'public', )
    form = CollegeTextHistoryAdminForm

""" Документы """
@admin.register(CollegeDocsModel)
class CollegeDocsAdmin(TranslationAdmin):
    list_display = ('id', 'public','college_license', 'college_reg', )

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
    list_display = ('title', 'public', 'file', )

""" Педагогический совет """
@admin.register(PedagogicalCouncilModel)
class PedagogicalCouncilAdmin(TranslationAdmin):
    list_display = ('title', 'public', 'file', )

""" Индустриальный совет """
@admin.register(IndustrialCouncilModel)
class IndustrialCouncilAdmin(TranslationAdmin):
    list_display = ('title', 'public', 'file', )

""" Галерея """
@admin.register(GalleryModel)
class GalleryAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'image', 'public', )