from django.db import models


""" Противодействие коррупции """
class AntiCorruptionModel(models.Model): 
    title = models.CharField( max_length=255, verbose_name='Наименование документа')
    file = models.FileField(upload_to="uploads/state/anti-corruption/",verbose_name="Документ")
    public = models.BooleanField(verbose_name='Опубликовать', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Противодействие коррупции'
        verbose_name_plural = 'Противодействие коррупции'

    def __str__(self) -> str:
        return self.title

""" Государственные Символы """
class StateSymbolsModel(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    image = models.ImageField(verbose_name='Изображение', upload_to = 'upload/state-symbols/', blank=True)
    desc = models.TextField(verbose_name='Описание', blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Государственные Символы'
        verbose_name_plural = 'Государственные Символы'

    def __str__(self) -> str:
        return self.name

""" Послание президента """
class PresidentialMessageModel(models.Model):
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст', blank=True)
    image = models.FileField(upload_to="uploads/state/presidential-message/", verbose_name="Изображение", blank=True)
    is_public = models.BooleanField(verbose_name='Опубликовать', default=False)

    created = models.DateTimeField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Послание президента'
        verbose_name_plural = 'Послание президента'

    def __str__(self) -> str:
        return self.title


""" Государственные услуги """
class StateServicesModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование документа')
    file = models.FileField(upload_to="uploads/state/state-services/",verbose_name="Документ")
    public = models.BooleanField(verbose_name='Опубликовать', default=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Документ государственных услуг'
        verbose_name_plural = 'Документ государственных услуг'

    def __str__(self) -> str:
        return self.title
    
""" Программа полиязычия """
class PolyiyasiaProgramModel(models.Model):
    title = models.CharField(max_length=255,  verbose_name='Наименование документа')
    file = models.FileField(upload_to='uploads/state/polyiyasia-program/', verbose_name='Документ')
    public = models.BooleanField(default=True, verbose_name='Опубликовать')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Документ программы полиязычия'
        verbose_name_plural = 'Документ программы полиязычия'

    def __str__(self) -> str:
        return self.title