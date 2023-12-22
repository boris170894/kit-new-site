from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import (
                        CollegePartnersModel,
                     )

@admin.register(CollegePartnersModel)
class CollegePartnersAdmin(TranslationAdmin):
    list_display = ('partner_name',)