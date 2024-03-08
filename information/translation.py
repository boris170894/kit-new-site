from modeltranslation.translator import register, TranslationOptions
from .models import (
                        CollegeContactModel, 
                        StudentEventModel,
                        MetodicRecomendationsCategoryModel,
                        MetodicRecomendationsDocumentModel,
                        FinancialStatementsModel,
                        CollegeDocsModel,
                        MainAdvantagesOfOurCollegeModel,
                        LibraryModel,
                        LibraryFilesModel,
                        DormitoryFilesModel,
                        DormitoryModel,
                    )

""" Контакты """
@register(CollegeContactModel)
class CollegeContactTransOptions(TranslationOptions):
    fields = ('addr',)

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
    fields = ('text', )

""" Библиотека, файлы """
@register(LibraryFilesModel)
class LibraryTransOptions(TranslationOptions):
    fields = ('title', 'file', )


""" Общежитие файлы """
@register(DormitoryFilesModel)
class DormitoryFilesTransOptions(TranslationOptions):
    fields = ('title', 'file' )

""" Общежитие """
@register(DormitoryModel)
class DormitoryTransOptions(TranslationOptions):
    fields = ('about', )