from modeltranslation.translator import register, TranslationOptions
from .models import (CollegeHistoryModel,
                        CollegeDocsModel,
                        BoardOfTrusteesModel,
                        PedagogicalCouncilModel,
                        IndustrialCouncilModel,
                        SpecInfoModel,
                        CollegeTextHistoryModel,
                        GalleryModel,
                    )

""" История колледжа события """
@register(CollegeHistoryModel)
class CollegeHistoryTransOptions(TranslationOptions):
    fields = ('info',)

""" История колледжа текст """
@register(CollegeTextHistoryModel)
class CollegeTextHistoryTransOptions(TranslationOptions):
    fields = ('text', 'our_mission')

""" Документы """
@register(CollegeDocsModel)
class CollegeDocsTransOptions(TranslationOptions):
    fields = ('college_license', 'college_reg', )

""" Специальности """
@register(SpecInfoModel)
class SpecInfoTransOptions(TranslationOptions):
    fields = ('spec_name','spec_info', )

""" Попечительский совет """
@register(BoardOfTrusteesModel)
class BoardOfTrusteesTransOptions(TranslationOptions):
    fields = ('title', 'file',)

""" Педагогический совет """
@register(PedagogicalCouncilModel)
class PedagogicalCouncilTransOptions(TranslationOptions):
    fields = ('title', 'file',)

""" Индустриальный совет """
@register(IndustrialCouncilModel)
class IndustrialCouncilTransOptions(TranslationOptions):
    fields = ('title', 'file',)

""" Галерея """
@register(GalleryModel)
class GalleryTransOptions(TranslationOptions):
    fields = ('title', )