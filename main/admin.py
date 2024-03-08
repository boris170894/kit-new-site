from django.contrib import admin
from django import forms
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import (CollegePartnersModel,

                    CollegeSliderModel,
                    CollegeSliderImageModel,

                    ThemesModel,

                    SocialMediaLinksModel,
                    NewSocialMediaLinkModel,

                    SliderForDocumentListModel,
                    SliderForDocumentListSlideModel)

""" Партнеры колледжа """
@admin.register(CollegePartnersModel)
class CollegePartnersAdmin(TranslationAdmin):
    list_display = ('partner_name',)

class CollegeSliderAdminForm(forms.ModelForm):
    text_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[ru]')
    text_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[kk]')
    text_en = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[en]')

    class Meta:
        model = CollegeSliderModel
        fields = '__all__'

""" Слайдер на главной странице  """
@admin.register(CollegeSliderModel)
class CollegeSliderAdmin(TranslationAdmin):
    form = CollegeSliderAdminForm
    list_display = ('title', 'public')

""" Изображения для слайдера на главной странице """
@admin.register(CollegeSliderImageModel)
class CollegeSliderImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'public', 'update_date', )

""" Темы """
@admin.register(ThemesModel)
class ThemesAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_gray_theme', )

""" Новая социальная сеть """
@admin.register(NewSocialMediaLinkModel)
class NewSocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'public', 'update_date', )

""" Ссылки на социальные сети """
@admin.register(SocialMediaLinksModel)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'update_date', )

""" Слайдер для страниц с документами """
@admin.register(SliderForDocumentListModel)
class SliderForDocumentListAdmin(admin.ModelAdmin):
    list_display = ('page', 'updated')

""" Слайд для слайдера для страниц с документами """
@admin.register(SliderForDocumentListSlideModel)
class SliderForDocumentListSlideAdmin(TranslationAdmin):
    list_display = ('id', 'image', 'is_public', 'updated', )
