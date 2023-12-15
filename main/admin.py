from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import (
                        CollegeContactModel, 
                        CollegePartnersModel,
                        StateSymbolsModel,
                        CallPairScheduleModel,
                        AcademicProcessScheduleModel,
                        StudentEventModel,
                        MetodicRecomendationsCategoryModel,
                        MetodicRecomendationsDocumentModel
                     )

@admin.register(CollegeContactModel)
class CollegeContactAdmin(TranslationAdmin):
    list_display = ('addr',)

@admin.register(CollegePartnersModel)
class CollegePartnersAdmin(TranslationAdmin):
    list_display = ('partner_name',)

@admin.register(StudentEventModel)
class StudentEventsAdmin(TranslationAdmin):
    list_display = ('title', 'description', )
    
admin.site.register(CallPairScheduleModel)
admin.site.register(AcademicProcessScheduleModel)

@admin.register(StateSymbolsModel)
class StateSymbolsAdmin(TranslationAdmin):
    list_display = ('name', 'image',)

@admin.register(MetodicRecomendationsCategoryModel)
class MetodicRecomendationsCategoryAdmin(TranslationAdmin):
    list_display = ('title', 'is_for_student', 'is_for_teacher', )

@admin.register(MetodicRecomendationsDocumentModel)
class MetodicRecomendationsDocumentAdmin(TranslationAdmin):
    list_display = ('title', 'category', 'updated', )