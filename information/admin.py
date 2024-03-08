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
                        LibraryModel,
                        LibraryFilesModel,
                        LibrarySliderImageModel,
                        DormitoryModel,
                        DormitoryFilesModel,
                        DormitoryImagesModel,
                        DormitoryContactsEmailModel,
                        DormitoryContactsPhoneModel,
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


""" Библиотека """
class LibraryAdminForm(forms.ModelForm):
    text_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[ru]')
    text_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[kk]')
    text_en = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[en]')

    class Meta:
        model = LibraryModel
        fields = '__all__'

""" События для студентов """
@admin.register(LibraryModel)
class LibraryAdmin(TranslationAdmin):
    list_display = ('id', 'is_public', 'updated', )
    form = LibraryAdminForm

""" Библиотека, изображения для слайдера """
@admin.register(LibrarySliderImageModel)
class LibrarySliderImageModel(admin.ModelAdmin):
    list_display = ('id', 'image', 'is_public', 'updated', )

""" Библиотека, файлы """
@admin.register(LibraryFilesModel)
class LibraryFilesAdmin(TranslationAdmin):
    list_display = ('title', 'is_public', 'updated', )

class DormitoryAdminForm(forms.ModelForm):
    about_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[ru]')
    about_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[kk]')
    about_en = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[en]')
    class Meta:
        model = DormitoryModel
        fields = '__all__'

""" Общежитие """
@admin.register(DormitoryModel)
class DormitoryAdmin(TranslationAdmin):
    list_display = ('id', 'updated', )
    form  = DormitoryAdminForm

""" Общежитие Загрузка файлов """
@admin.register(DormitoryFilesModel)
class DormitoryFilesAdmin(TranslationAdmin):
    list_display = ('title', 'is_public', 'updated', )

""" Общежитие Загрузка фото """
@admin.register(DormitoryImagesModel)
class DormitoryImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'is_public', 'updated', )

admin.site.register(DormitoryContactsEmailModel)
admin.site.register(DormitoryContactsPhoneModel)