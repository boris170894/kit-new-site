from modeltranslation.translator import register, TranslationOptions
from .models import SpecInfoModel

@register(SpecInfoModel)
class SpecInfoTransOptions(TranslationOptions):
    fields = (
        'spec_name',
        'spec_info',
    )