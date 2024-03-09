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

""" Слайдер на главной странице """
class CollegeSliderModel(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100, blank=True)
    text = models.TextField(verbose_name='Описание', blank=True)
    public = models.BooleanField(verbose_name='Опубликовано', default=False)

    class Meta:
        verbose_name = 'Cлайдер на главной странице'
        verbose_name_plural = 'Cлайдер на главной странице'

    def __str__(self) -> str:
        return self.title

""" Изображения для слайдера на главной странице """
class CollegeSliderImageModel(models.Model):
    college_slider = models.ForeignKey(CollegeSliderModel, verbose_name='Слад', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='uploads/slider/', blank=True)

    status_1 = models.BooleanField(verbose_name='Отметить как главное изображение', default=False)
    status_2 = models.BooleanField(verbose_name='Отметить как второе изображение', default=False)
    status_3 = models.BooleanField(verbose_name='Отметить как третье изображение', default=False)

    public = models.BooleanField(verbose_name='Опубликовано', default=False)

    create_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Изображение слайдера на главной странице'
        verbose_name_plural = 'Изображение слайдера на главной странице'

    def __str__(self) -> str:
        return self.college_slider.title

""" Темы  """
class ThemesModel(models.Model):
    is_gray_theme = models.BooleanField(verbose_name='Серая тема', default=False)

    class Meta:
        verbose_name = 'Расцветка сайта'
        verbose_name_plural = 'Расцветка сайта'

""" Новая социальная сеть """
class NewSocialMediaLinkModel(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название", unique=True)
    link = models.URLField(verbose_name="Ссылка на сайт")
    icon_file = models.FileField(verbose_name="Загрузить иконку", upload_to='uploads/socialMedias', blank=True)
    icon_link = models.URLField(verbose_name="Ссылка на иконку", blank=True)

    public = models.BooleanField(verbose_name="Опубликовать", default=False, blank=True)

    create_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Новая социальная сеть'
        verbose_name_plural = 'Новая социальная сеть'

    def __str__(self) -> str:
        return self.title


""" Ссылки на социальные сети  """
class SocialMediaLinksModel(models.Model):
    instagram = models.URLField(verbose_name="Ссылка Instagram", blank=True)
    facebook = models.URLField(verbose_name="Ссылка Facebook", blank=True)
    youtube = models.URLField(verbose_name="Ссылка YouTube", blank=True)
    telegram = models.URLField(verbose_name="Ссылка Telegram", blank=True)
    tiktok = models.URLField(verbose_name="Ссылка TikTok", blank=True)

    other_medias = models.ManyToManyField(NewSocialMediaLinkModel, blank=True, default=[])

    create_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Ссылки на социальные сети'
        verbose_name_plural = 'Ссылки на социальные сети'


""" Слайдер для страниц с документами """
class SliderForDocumentListModel(models.Model):
    PAGES = (
        ('Общая информация', 'Общая информация'),
        ('Кружки и секции', 'Кружки и секции'),
        ('Психологическая служба', 'Психологическая служба'),
        ('Противодействие коррупции', 'Противодействие коррупции'),
        ('Программа полиязычия', 'Программа полиязычия'),
        ('Попечительский совет', 'Попечительский совет'),
        ('Педагогический совет', 'Педагогический совет'),
        ('Индустриальный совет', 'Индустриальный совет'),
    )
    page = models.CharField(max_length=100, choices=PAGES, verbose_name='Страница')
    images = models.ManyToManyField('SliderForDocumentListSlideModel', verbose_name='Слайды', default=[], blank=True)

    is_public = models.BooleanField(verbose_name='Опубликовать', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Слайдер для страниц с документами'
        verbose_name_plural = 'Слайдер для страниц с документами'

    def __str__(self) -> str:
        return f'{self.id}. {self.page}'

""" Слайд для слайдера для страниц с документами """
class SliderForDocumentListSlideModel(models.Model):
    image = models.ImageField(upload_to=f"uploads/main/documents-slider/slides/", verbose_name='Слайд')
    is_public = models.BooleanField(verbose_name='Опубликовать', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Слайд для слайдера для страниц с документами'
        verbose_name_plural = 'Слайд для слайдера для страниц с документами'

    def __str__(self) -> str:
        return f"{self.id} - {self.updated}"