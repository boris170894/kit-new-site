from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import (CollegeHistoryModel,
                                    CollegeDocsModel, 
                                    BoardOfTrusteesModel,
                                    PedagogicalCouncilModel,
                                    IndustrialCouncilModel )


@admin.register(CollegeHistoryModel)
class CollegeHistoryAdmin(TranslationAdmin):
    list_display = ('year',)

admin.site.register(CollegeDocsModel)

@admin.register(BoardOfTrusteesModel)
class BoardOfTrusteesAdmin(TranslationAdmin):
    list_display = ('title', 'file', 'public', )

@admin.register(PedagogicalCouncilModel)
class PedagogicalCouncilAdmin(TranslationAdmin):
    list_display = ('title', 'file', 'public', )

@admin.register(IndustrialCouncilModel)
class IndustrialCouncilAdmin(TranslationAdmin):
    list_display = ('title', 'file', 'public', )