from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import  (GeneralInformationFilesModel, 
                        ClubsAndSectionsModel, ClubsAndSectionsDocumentsModel,
                        PsychologicalServiceModel,
                        YouthPolicyModel, YouthPolicyFilesModel, YouthPolicyImagesModel, TerrorModel
                        )
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


""" Общая информация """
@admin.register(GeneralInformationFilesModel)
class GeneralInformationFilesAdmin(TranslationAdmin):
    list_display = ('title', 'updated', )

class ClubsAndSectionsAdminForm(forms.ModelForm):
    about_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[ru]')
    about_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[kk]')
    about_en = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[en]')
    class Meta:
        model = ClubsAndSectionsModel
        fields = '__all__'

""" Кружки и секции """
@admin.register(ClubsAndSectionsModel)
class ClubsAndSectionsAdmin(TranslationAdmin):
    list_display = ('title', 'updated', )
    form = ClubsAndSectionsAdminForm

""" Файлы  кружков и секций """
@admin.register(ClubsAndSectionsDocumentsModel)
class ClubsAndSectionsDocumentsAdmin(TranslationAdmin):
    list_display = ('title', 'category',  'public', 'file', )

""" Психологическая служба """
@admin.register(PsychologicalServiceModel)
class PsychologicalServiceAdmin(TranslationAdmin):
    list_display = ('title', 'is_public', 'updated', 'file', )

class YouthPolicyAdminForm(forms.ModelForm):
    about_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание [ru]')
    about_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание [kk]')
    about_en = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание [en]')
    class Meta:
        model = YouthPolicyModel
        fields = '__all__'

""" Молодежная политика """
@admin.register(YouthPolicyModel)
class YouthPolicyAdmin(TranslationAdmin):
    list_display = ('id', 'updated', )
    form = YouthPolicyAdminForm

""" Молодежная политика Загрузка файлов """
@admin.register(YouthPolicyFilesModel)
class YouthPolicyFilesAdmin(TranslationAdmin):
    list_display = ('title', 'is_public', 'updated', )

""" Молодежная политика Загрузка фото """
@admin.register(YouthPolicyImagesModel)
class YouthPolicyImagesAdmin(TranslationAdmin):
    list_display = ('id', 'file', 'is_public', 'updated', )


""" Терроризм и т.д. и т.п. """
@admin.register(TerrorModel)
class TerrorAdmin(TranslationAdmin):
    list_display = ('id','title')