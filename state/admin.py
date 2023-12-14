from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import AntiCorruptionModel

@admin.register(AntiCorruptionModel)
class AntiCorruptionsAdmin(TranslationAdmin):
    list_display = ('id', 'updated', 'title1', 'title2', 'title3', )
