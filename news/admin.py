from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin

from .models import CategoryModel, NewsModel

@admin.register(CategoryModel)
class CategoryAdmin(TranslationAdmin):
    list_display = ('category_name_ru',)

class NewsAdminForm(forms.ModelForm):
    news_content_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[ru]')
    news_content_kk = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[kk]')
    news_content_en = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент_[en]')
    class Meta:
        model = NewsModel
        fields = '__all__'

@admin.register(NewsModel)
class NewsAdmin(TranslationAdmin):

    prepopulated_fields = {"slug":("news_title",)}
    form = NewsAdminForm

    list_per_page = 10

    list_filter = ('news_category', 'news_is_published')

    list_display = (
        "news_title",
        "news_category",
        "news_is_published",
        
        "news_create_date",  # Выводим дату создания
        "news_update_date",  # Выводим дату обновления
    )

    search_fields = ("news_title",)

    list_editable = ("news_is_published",)