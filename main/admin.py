from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import (
                        CollegePartnersModel,
                        CollegeSliderModel,
                     )

""" Партнеры колледжа """
@admin.register(CollegePartnersModel)
class CollegePartnersAdmin(TranslationAdmin):
    list_display = ('partner_name',)

""" Слайдер колледжа """
@admin.register(CollegeSliderModel)
class CollegeSliderAdmin(TranslationAdmin):
    list_display = ('number', 'title', 'public')