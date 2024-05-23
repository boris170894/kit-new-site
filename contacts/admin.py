from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import CollegeContactModel

""" Контакты """
@admin.register(CollegeContactModel)
class CollegeContactAdmin(TranslationAdmin):
    list_display = ('addr', 'e_mail', 'tel', 'priem_com', 'wats', )
