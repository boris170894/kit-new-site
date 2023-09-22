from django.db import models

""" История колледжа """
class CollegeHistoryModel(models.Model):

    year = models.DateField(verbose_name='Дата события')
    info = models.TextField(verbose_name='Описание')

    def __str__(self):
        return str(self.year)
    
    class Meta:
        verbose_name = 'История колледжа'
        verbose_name_plural = 'История колледжа'

""" Контакты """
class CollegeContactModel(models.Model):

    addr = models.CharField(verbose_name='Адрес', max_length=300)
    e_mail = models.CharField(verbose_name='e-mail', max_length=20)
    tel = models.CharField(verbose_name='Телефон', max_length=20)
    priem_com = models.CharField(verbose_name='Приёмная комиссия', max_length=20)
    wats = models.CharField(verbose_name='Watsapp', max_length=20)


    def __str__(self):
        return("Информация")
    
    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


""" Партнеры колледжа """
class CollegePartnersModel(models.Model):

    partner_name = models.CharField(verbose_name='Наименование', max_length=200)
    partner_logo = models.ImageField(verbose_name='Лого', upload_to = 'upload/partners', blank=True)
    partner_url = models.CharField(verbose_name='Ссылка на сайт', max_length=100, blank=True)

    def __str__(self):
        return self.partner_name
    
    class Meta:
        verbose_name = 'Партнёры колледжа'
        verbose_name_plural = 'Партнёры колледжа'

""" Документы """
class CollegeDocsModel(models.Model):

    college_license = models.FileField(upload_to="uploads/Docs",verbose_name="Лицензия")
    college_reg = models.FileField(upload_to="uploads/Docs",verbose_name="Устав")

    class Meta:
        verbose_name = 'Документы колледжа'
        verbose_name_plural = 'Документы колледжа'

""" Государственные Символы """
class StateSymbolsModel(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255, blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to = 'upload/state-symbols', blank=True)
    desc = models.TextField(verbose_name='Описание', blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Государственные Символы'
        verbose_name_plural = 'Государственные Символы'

# """ Государственные Символы """
# class StateSymbolsModel(models.Model):
    
#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = ''
#         verbose_name_plural = ''