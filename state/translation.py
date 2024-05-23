from modeltranslation.translator import register, TranslationOptions
from .models import (AntiCorruptionModel, 
                        StateSymbolsModel,
                        StateServicesModel,
                        PolyiyasiaProgramModel,
                        PresidentialMessageModel)

""" Противодействие коррупции """
@register(AntiCorruptionModel)
class AntiCorruptionTransOptions(TranslationOptions):
    fields = ('title', 'file', )

""" Государственные Символы """
@register(StateSymbolsModel)
class StateSymbolsTransOptions(TranslationOptions):
    fields = ('name', 'desc', )

""" Послание президента """
@register(PresidentialMessageModel)
class PresidentialMessageTransOptions(TranslationOptions):
    fields = ('title', 'text',)

""" Государственные услуги """
@register(StateServicesModel)
class StateServicesTransOptions(TranslationOptions):
    fields = ('title', )

""" Программа полиязычия """
@register(PolyiyasiaProgramModel)
class PolyiyasiaProgramTransOptions(TranslationOptions):
    fields = ('title', 'file', )
