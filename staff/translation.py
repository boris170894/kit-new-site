from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(DirectorModel)
class CyclicMCTransOptions(TranslationOptions):
    fields = ('info',)

@register(DepDirectorModel)
class CyclicMCTransOptions(TranslationOptions):
    fields = ('info',)

@register(DepHeadModel)
class CyclicMCTransOptions(TranslationOptions):
    fields = ('info',)

@register(CmcOBModel)
class CyclicMCTransOptions(TranslationOptions):
    fields = ('info',)

@register(CmcLangModel)
class CyclicMCTransOptions(TranslationOptions):
    fields = ('info',)

@register(CmcELModel)
class CyclicMCTransOptions(TranslationOptions):
    fields = ('info',)

@register(CmcITModel)
class CyclicMCTransOptions(TranslationOptions):
    fields = ('info',)

@register(CmcFIZModel)
class CyclicMCTransOptions(TranslationOptions):
    fields = ('info',)

@register(PositionModel)
class CyclicMCTransOptions(TranslationOptions):
    fields = ('position_name',)