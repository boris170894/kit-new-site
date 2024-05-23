from modeltranslation.translator import register, TranslationOptions
from .models import (
                        AnnouncementVacanciesModel,
                        AnnouncementModel,
                        AnnouncementFilesModel,
                        AnnouncementImagesModel,
                    )


""" Объявления """
@register(AnnouncementModel)
class AnnouncementTransOptions(TranslationOptions):
    fields = ('about', 'video', )

""" Объявления, Загрузка файлов """
@register(AnnouncementFilesModel)
class AnnouncementFilesTransOptions(TranslationOptions):
    fields = ('title', 'file',)

""" Объявления, Загрузка фото """
@register(AnnouncementImagesModel)
class AnnouncementImagesTransOptions(TranslationOptions):
    fields = ('file', )

""" Объявления, Вакансии """
@register(AnnouncementVacanciesModel)
class AnnouncementVacanciesTransOptions(TranslationOptions):
    fields = ('title', 'description', )