from modeltranslation.translator import register, TranslationOptions
from .models import (
                        CollegeContactModel, 
                        CollegePartnersModel, 
                        StateSymbolsModel,
                        StudentEventModel,
                        MetodicRecomendationsCategoryModel,
                        MetodicRecomendationsDocumentModel,
                    )

@register(CollegeContactModel)
class CollegeContactTransOptions(TranslationOptions):
    fields = ('addr',)

@register(CollegePartnersModel)
class CollegePartnersTransOptions(TranslationOptions):
    fields = ('partner_name',)
    
@register(StateSymbolsModel)
class StateSymbolsModelTransOptions(TranslationOptions):
    fields = ('name', 'desc',)
    
@register(StudentEventModel)
class StudentEventTransOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(MetodicRecomendationsCategoryModel)
class MetodicRecomendationsCategoryTransOptions(TranslationOptions):
    fields = ('title',)

@register(MetodicRecomendationsDocumentModel)
class MetodicRecomendationsDocumentTransOptions(TranslationOptions):
    fields = ('title',)