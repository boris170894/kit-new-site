from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import RuleWorldSkillsModel, CompetentionModel, CompetentionDocumentationModel

@admin.register(RuleWorldSkillsModel)
class RuleWorldSkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'updated', )

@admin.register(CompetentionModel)
class CompetentionAdmin(TranslationAdmin):
    list_display = ('title',  )

@admin.register(CompetentionDocumentationModel)
class CompetentionDocumentationAdmin(TranslationAdmin):
    list_display = ('title', 'competention', 'updated', )