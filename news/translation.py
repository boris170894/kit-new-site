from modeltranslation.translator import register, TranslationOptions
from .models import CategoryModel, NewsModel

@register(CategoryModel)
class CategoryTransOptions(TranslationOptions):
    fields = ('category_name',)


@register(NewsModel)
class NewsTransOptions(TranslationOptions):
    fields = (
        'news_title',
        'news_content',
    )