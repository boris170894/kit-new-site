from django.db import models

""" Партнеры колледжа """
class CollegePartnersModel(models.Model):

    partner_name = models.CharField(verbose_name='Наименование', max_length=200)
    partner_logo = models.ImageField(verbose_name='Лого', upload_to = 'uploads/index-page/partners', blank=True)
    partner_url = models.CharField(verbose_name='Ссылка на сайт', max_length=100, blank=True)

    def __str__(self) -> str:
        return self.partner_name
    
    class Meta:
        verbose_name = 'Партнёры колледжа'
        verbose_name_plural = 'Партнёры колледжа'

""" Слайдер  """
class CollegeSliderModel(models.Model):
    number = models.CharField(verbose_name='Заголовок', max_length=30, blank=True)
    title = models.CharField(verbose_name='Название', max_length=100, blank=True)
    text = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to = 'uploads/slider', blank=True)
    image2 = models.ImageField(verbose_name='Изображение 2', upload_to = 'uploads/slider', blank=True)
    image3 = models.ImageField(verbose_name='Изображение 3', upload_to = 'uploads/slider', blank=True)
    public = models.BooleanField(verbose_name='Опубликовано', default=False)

    class Meta:
        verbose_name = 'Слайдер на главной странице'
        verbose_name_plural = 'Слайдер на главной странице'

    def __str__(self) -> str:
        return self.title