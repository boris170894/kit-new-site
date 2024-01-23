from modeltranslation.translator import register, TranslationOptions
from .models import (AntiCorruptionModel, 
                                    StateSymbolsModel,
                                    StateServicesModel,
                                    PolyiyasiaProgramModel)

@register(AntiCorruptionModel)
class AntiCorruptionTransOptions(TranslationOptions):
    fields = ('title', )

@register(StateSymbolsModel)
class StateSymbolsTransOptions(TranslationOptions):
    fields = ('name', 'desc', )
    
@register(StateServicesModel)
class StateServicesTransOptions(TranslationOptions):
    fields = ('title', )

@register(PolyiyasiaProgramModel)
class PolyiyasiaProgramTransOptions(TranslationOptions):
    fields = ('title', )