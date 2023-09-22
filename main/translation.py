from modeltranslation.translator import register, TranslationOptions
from .models import (
                        CollegeHistoryModel, 
                        CollegeContactModel, 
                        CollegePartnersModel, 
                        StateSymbolsModel
                    )

@register(CollegeHistoryModel)
class CollegeHistoryTransOptions(TranslationOptions):
    fields = ('info',)


@register(CollegeContactModel)
class CollegeContactTransOptions(TranslationOptions):
    fields = ('addr',)

@register(CollegePartnersModel)
class CollegePartnersTransOptions(TranslationOptions):
    fields = ('partner_name',)
    
@register(StateSymbolsModel)
class StateSymbolsModelTransOptions(TranslationOptions):
    fields = ('name', 'desc',)
    