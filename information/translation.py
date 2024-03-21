from modeltranslation.translator import register, TranslationOptions
from .models import (
                        StudentEventModel,
                        MetodicRecomendationsCategoryModel,
                        MetodicRecomendationsDocumentModel,
                        FinancialStatementsModel,
                        CollegeDocsModel,
                        MainAdvantagesOfOurCollegeModel,
                        LibraryModel,
                        LibraryFilesModel,
                        DormitoryFilesModel, DormitoryModel, DormitoryImagesModel,
                        OurUnionModel, OurUnionFilesModel, OurUnionImagesModel
                    )


""" Расписание звонков и основное расписание """
@register(StudentEventModel)
class StudentEventTransOptions(TranslationOptions):
    fields = ('title', 'description',)

""" Категории методических рекомендаций """
@register(MetodicRecomendationsCategoryModel)
class MetodicRecomendationsCategoryTransOptions(TranslationOptions):
    fields = ('title',)

""" Файлы методических рекомендаций """
@register(MetodicRecomendationsDocumentModel)
class MetodicRecomendationsDocumentTransOptions(TranslationOptions):
    fields = ('title',)

""" Финансовая отчетность """
@register(FinancialStatementsModel)
class FinancialStatementsTransOptions(TranslationOptions):
    fields = ('title',)

""" Перечень необходимых документов """
@register(CollegeDocsModel)
class CollegeDocsTransOptions(TranslationOptions):
    fields = ('title',)

""" Основные преимущества нашего колледжа """
@register(MainAdvantagesOfOurCollegeModel)
class AdvancesOfOurCollegeTransOptions(TranslationOptions):
    fields = ('title',)

""" Библиотека """
@register(LibraryModel)
class LibraryTransOptions(TranslationOptions):
    fields = ('text', 'video' )

""" Библиотека, файлы """
@register(LibraryFilesModel)
class LibraryTransOptions(TranslationOptions):
    fields = ('title', 'file', )

""" Общежитие """
@register(DormitoryModel)
class DormitoryTransOptions(TranslationOptions):
    fields = ('about', 'video')

""" Общежитие файлы """
@register(DormitoryFilesModel)
class DormitoryFilesTransOptions(TranslationOptions):
    fields = ('title', 'file',)

""" Общежитие фото """
@register(DormitoryImagesModel)
class DormitoryImagesTransOptions(TranslationOptions):
    fields = ('file',)

""" Наш профсоюз """
@register(OurUnionModel)
class OurUnionTransOptions(TranslationOptions):
    fields = ('about', 'video', )

""" Наш профсоюз файлы """
@register(OurUnionFilesModel)
class OurUnionFilesTransOptions(TranslationOptions):
    fields = ('title', 'file',)

""" Молодежная политика фото """
@register(OurUnionImagesModel)
class OurUnionImagesTransOptions(TranslationOptions):
    fields = ('file', )