from modeltranslation.translator import register, TranslationOptions
from .models import (
                                GroupModel,
                                CMCModel,
                                PositionModel,
                                PersonModel
                            )

""" Группа """
@register(GroupModel)
class GroupTransOptions(TranslationOptions):
    fields = ('name',)

""" ЦМК """
@register(CMCModel)
class CMCTransOptions(TranslationOptions):
    fields = ('title',)

""" Должность """
@register(PositionModel)
class PositionTransOptions(TranslationOptions):
    fields = ('title',)

""" Персонал """
@register(PersonModel)
class PersonalTransOptions(TranslationOptions):
    fields = ('fio', 'info')