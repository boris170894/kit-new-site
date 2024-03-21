from modeltranslation.translator import register, TranslationOptions
from .models import CollegeContactModel


""" Контакты """
@register(CollegeContactModel)
class CollegeContactTransOptions(TranslationOptions):
    fields = ('addr', 'workSchedule', )