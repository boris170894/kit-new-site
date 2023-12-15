from modeltranslation.translator import register, TranslationOptions
from .models import (CollegeHistoryModel, 
                                    BoardOfTrusteesModel,
                                    PedagogicalCouncilModel,
                                    IndustrialCouncilModel )

@register(CollegeHistoryModel)
class CollegeHistoryTransOptions(TranslationOptions):
    fields = ('info',)

@register(BoardOfTrusteesModel)
class BoardOfTrusteesTransOptions(TranslationOptions):
    fields = ('title',)

@register(PedagogicalCouncilModel)
class PedagogicalCouncilTransOptions(TranslationOptions):
    fields = ('title',)

@register(IndustrialCouncilModel)
class IndustrialCouncilTransOptions(TranslationOptions):
    fields = ('title',)