from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import (
                        CollegeContactModel, 
                        StudentEventModel,
                        MetodicRecomendationsCategoryModel,
                        MetodicRecomendationsDocumentModel,
                        FinancialStatementsModel,
                        CallPairScheduleModel,
                        AcademicProcessScheduleModel,
                        CollegeDocsModel,
                        MainAdvantagesOfOurCollegeModel,
                    )

""" Контакты """
@admin.register(CollegeContactModel)
class CollegeContactAdmin(TranslationAdmin):
    list_display = ('addr', 'e_mail', 'tel', 'priem_com', 'wats', )

""" Расписание звонков и основное расписание """ 
admin.site.register(CallPairScheduleModel)

""" График Учебного процесса """
admin.site.register(AcademicProcessScheduleModel)

class StudentEventsAdminForm(forms.ModelForm):
    description_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[ru]')
    description_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[kk]')
    description_en = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[en]')
    class Meta:
        model = StudentEventModel
        fields = '__all__'

""" События для студентов """
@admin.register(StudentEventModel)
class StudentEventsAdmin(TranslationAdmin):
    list_display = ('title', 'description', )
    form = StudentEventsAdminForm

""" Категории методических рекомендаций """
@admin.register(MetodicRecomendationsCategoryModel)
class MetodicRecomendationsCategoryAdmin(TranslationAdmin):
    list_display = ('title', 'is_for_student', 'is_for_teacher', )

""" Файлы методических рекомендаций """
@admin.register(MetodicRecomendationsDocumentModel)
class MetodicRecomendationsDocumentAdmin(TranslationAdmin):
    list_display = ('title', 'category', 'updated', )

""" Финансовая отчетность """
@admin.register(FinancialStatementsModel)
class FinancialStatementsAdmin(TranslationAdmin):
    list_display = ('title', 'is_public', 'updated', 'file', )

""" Перечень необходимых документов """
@admin.register(CollegeDocsModel)
class CollegeDocsAdmin(TranslationAdmin):
    list_display = ('title', 'is_public', )

""" Основные преимущества нашего колледжа """
@admin.register(MainAdvantagesOfOurCollegeModel)
class MainAdvantagesOfOurCollegeAdmin(TranslationAdmin):
    list_display = ('title', 'is_public', )