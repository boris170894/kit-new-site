from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import  (GeneralInformationFilesModel, 
                                ClubsAndSectionsModel,
                                ClubsAndSectionsDocumentsModel,
                                PsychologicalServiceModel,
                                DormitoryModel,
                                DormitoryFilesModel,
                                DormitoryImagesModel,
                                DormitoryContactsEmailModel,
                                DormitoryContactsPhoneModel,
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