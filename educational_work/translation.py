from modeltranslation.translator import register, TranslationOptions 
from .models import  (GeneralInformationFilesModel, 
                        ClubsAndSectionsModel, ClubsAndSectionsDocumentsModel,
                        PsychologicalServiceModel,
                        YouthPolicyModel, YouthPolicyFilesModel, YouthPolicyImagesModel,
                        TerrorModel
                      )

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

""" Молодежная политика """
@register(YouthPolicyModel)
class YouthPolicyTransOptions(TranslationOptions):
    fields = ('about', )

""" Молодежная политика файлов """
@register(YouthPolicyFilesModel)
class YouthPolicyFilesTransOptions(TranslationOptions):
    fields = ('title', 'file', )

""" Молодежная политика фото """
@register(YouthPolicyImagesModel)
class YouthPolicyImagesTransOptions(TranslationOptions):
    fields = ('file', )


""" Терроризм и т.д. и т.п. """
@register (TerrorModel)
class TerrorModel(TranslationOptions):
    fields = ('title',)