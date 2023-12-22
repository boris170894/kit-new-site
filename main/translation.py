from modeltranslation.translator import register, TranslationOptions
from .models import (
                        CollegePartnersModel, 
                    )

""" Партнеры колледжа """
@register(CollegePartnersModel)
class CollegePartnersTransOptions(TranslationOptions):
    fields = ('partner_name',)
