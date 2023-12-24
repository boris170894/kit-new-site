from modeltranslation.translator import register, TranslationOptions
from .models import (
                        CollegePartnersModel, 
                        CollegeSliderModel,
                    )

""" Партнеры колледжа """
@register(CollegePartnersModel)
class CollegePartnersTransOptions(TranslationOptions):
    fields = ('partner_name',)

""" Слайдер колледжа """
@register(CollegeSliderModel)
class CollegeSliderTransOptions(TranslationOptions):
    fields = ('title', 'number', 'text')

