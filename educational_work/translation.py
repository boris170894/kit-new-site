from modeltranslation.translator import register, TranslationOptions 
from .models import  (GeneralInformationFilesModel, 
                                        ClubsAndSectionsModel, 
                                        ClubsAndSectionsDocumentsModel,
                                        PsychologicalServiceModel, 
                                        DormitoryFilesModel, 
                                        DormitoryModel)

""" Общая информация """
@register(GeneralInformationFilesModel)
class GeneralInformationFilesTransOptions(TranslationOptions):
    fields = ('title', )

""" Кружки и секции """
@register(ClubsAndSectionsModel)
class ClubsAndSectionsTransOptions(TranslationOptions):
    fields = ('title', 'about' )

""" Файлы  кружков и секций """
@register(ClubsAndSectionsDocumentsModel)
class ClubsAndSectionsDocumentsTransOptions(TranslationOptions):
    fields = ('title', )

""" Психологическая служба """
@register(PsychologicalServiceModel)
class PsychologicalServiceTransOptions(TranslationOptions):
    fields = ('title', )

""" Общежитие файлы """
@register(DormitoryFilesModel)
class DormitoryFilesTransOptions(TranslationOptions):
    fields = ('title', )

""" Общежитие """
@register(DormitoryModel)
class DormitoryTransOptions(TranslationOptions):
    fields = ('about', )