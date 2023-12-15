from modeltranslation.translator import register, TranslationOptions 
from .models import  GeneralInformationFilesModel

@register(GeneralInformationFilesModel)
class GeneralInformationFilesTransOptions(TranslationOptions):
    fields = ('title', )