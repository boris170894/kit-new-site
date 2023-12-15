from django.db import models

""" История колледжа """
class CollegeHistoryModel(models.Model):

    year = models.DateField(verbose_name='Дата события')
    info = models.TextField(verbose_name='Описание')
    public = models.BooleanField(verbose_name='Опубликовать', default=True)

    def __str__(self):
        return str(self.year)
    
    class Meta:
        verbose_name = 'История колледжа'
        verbose_name_plural = 'История колледжа'

""" Документы """
class CollegeDocsModel(models.Model):

    college_license = models.FileField(upload_to="uploads/Docs",verbose_name="Лицензия")
    college_reg = models.FileField(upload_to="uploads/about_college/docs",verbose_name="Устав")
    public = models.BooleanField(verbose_name='Опубликовать', default=True)

    class Meta:
        verbose_name = 'Документы колледжа'
        verbose_name_plural = 'Документы колледжа'

""" Попечительский совет """
class BoardOfTrusteesModel(models.Model):
    title = models.CharField(verbose_name='Наименование документа', max_length=255 )
    file = models.FileField(upload_to="uploads/about_college/board_of_trustees",verbose_name="Документ")
    public = models.BooleanField(verbose_name='Опубликовать', default=True)

    class Meta:
        verbose_name = 'Документ для попечительского совета'
        verbose_name_plural = 'Документ для попечительского совета'

    def __str__(self) -> str:
        return self.title

""" Педагогический совет """
class PedagogicalCouncilModel(models.Model):
    title = models.CharField(verbose_name='Наименование документа', max_length=255 )
    file = models.FileField(upload_to="uploads/about_college/pedagogical_council",verbose_name="Документ")
    public = models.BooleanField(verbose_name='Опубликовать', default=True)

    class Meta:
        verbose_name = 'Документ для педагогического совета'
        verbose_name_plural = 'Документ для педагогического совета'

    def __str__(self) -> str:
        return self.title

""" Индустриальный совет """
class IndustrialCouncilModel(models.Model):
    title = models.CharField(verbose_name='Наименование документа', max_length=255 )
    file = models.FileField(upload_to="uploads/about_college/industrial_council", verbose_name="Документ")
    public = models.BooleanField(verbose_name='Опубликовать', default=True)

    class Meta:
        verbose_name = 'Документ для индустриального совета'
        verbose_name_plural = 'Документ для индустриального совета'

    def __str__(self) -> str:
        return self.title