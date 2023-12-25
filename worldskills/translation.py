from modeltranslation.translator import register, TranslationOptions
from .models import CompetentionModel, CompetentionDocumentationModel

@register(CompetentionModel)
class CompetentionTransOptions(TranslationOptions):
    fields = ('title', )

@register(CompetentionDocumentationModel)
class CompetentionDocumentationTransOptions(TranslationOptions):
    fields = ('title', )