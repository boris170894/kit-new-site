from modeltranslation.translator import register, TranslationOptions
from .models import (CollegeHistoryModel, 
                                    BoardOfTrusteesModel,
                                    PedagogicalCouncilModel,
                                    IndustrialCouncilModel, 
                                    SpecInfoModel)

""" История колледжа """
@register(CollegeHistoryModel)
class CollegeHistoryTransOptions(TranslationOptions):
    fields = ('info',)

""" Специальности """
@register(SpecInfoModel)
class SpecInfoTransOptions(TranslationOptions):
    fields = ('spec_name','spec_info', )

""" Попечительский совет """
@register(BoardOfTrusteesModel)
class BoardOfTrusteesTransOptions(TranslationOptions):
    fields = ('title',)

""" Педагогический совет """
@register(PedagogicalCouncilModel)
class PedagogicalCouncilTransOptions(TranslationOptions):
    fields = ('title',)

""" Индустриальный совет """
@register(IndustrialCouncilModel)
class IndustrialCouncilTransOptions(TranslationOptions):
    fields = ('title',)