from django.db import models
from django.urls import reverse

""" Модель категории новостей """
class CategoryModel(models.Model):
    
    category_name = models.CharField(verbose_name='Наименование категории', max_length=100)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

""" Модель новостей """
class NewsModel(models.Model):

    news_title = models.CharField(verbose_name='Заголовок', max_length=150)
    slug = models.SlugField(unique=True, max_length=100, verbose_name='URL', db_index=True)
    news_img = models.ImageField(verbose_name='Фото', upload_to = 'upload/news/%Y/%m/%d', blank=True)
    news_content = models.TextField(verbose_name='Контент')

    news_category = models.ForeignKey('CategoryModel', on_delete=models.PROTECT, verbose_name='Категория')

    news_is_published = models.BooleanField(verbose_name='Опубликовать', default=False)
    news_is_worldskills = models.BooleanField(verbose_name='WorldSkills', default=False)
    news_is_achivment = models.BooleanField(verbose_name='Достижение', default=False)

    news_create_date = models.DateTimeField(auto_now_add=True)
    news_update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.news_title

    def get_absolute_url(self):
        return reverse('news_view', kwargs={'slug':self.slug})

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


