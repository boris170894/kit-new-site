from modeltranslation.translator import register, TranslationOptions 
from .models import  (GeneralInformationFilesModel, 
                        ClubsAndSectionsModel,
                        ClubsAndSectionsDocumentsModel,
                        PsychologicalServiceModel,)

""" Общая информация """
@register(GeneralInformationFilesModel)
class GeneralInformationFilesTransOptions(TranslationOptions):
    fields = ('title', 'file', )

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
    fields = ('title', 'file', )
