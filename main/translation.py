from modeltranslation.translator import register, TranslationOptions
from .models import (
                        CollegePartnersModel, 
                        CollegeSliderModel,
                        SliderForDocumentListSlideModel,
                        IntroLogosModel,
                    )

""" Логотипы и надписи на главной странице """
@register(IntroLogosModel)
class IntroLogosTransOptions(TranslationOptions):
    fields = ('years', 'text', 'image')

""" Партнеры колледжа """
@register(CollegePartnersModel)
class CollegePartnersTransOptions(TranslationOptions):
    fields = ('partner_name',)

""" Слайдер колледжа """
@register(CollegeSliderModel)
class CollegeSliderTransOptions(TranslationOptions):
    fields = ('title', 'text')

""" Слайд для слайдера для страниц с документами """
@register(SliderForDocumentListSlideModel)
class SliderForDocumentListSlideTransOptions(TranslationOptions):
    fields = ('image', )