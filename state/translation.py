from modeltranslation.translator import register, TranslationOptions
from .models import AntiCorruptionModel

@register(AntiCorruptionModel)
class AntiCorruptionTransOptions(TranslationOptions):
    fields = ('title1', 'title2', 'title3', )