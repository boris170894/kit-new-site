from django.db import models

""" Правила """
class RuleWorldSkillsModel(models.Model):
    file1 = models.FileField(verbose_name='Файл 1', upload_to="uploads/worldskills/rules/", blank=True)
    file2 = models.FileField(verbose_name='Файл 2', upload_to="uploads/worldskills/rules/", blank=True)
    file3 = models.FileField(verbose_name='Файл 3', upload_to="uploads/worldskills/rules/", blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Правила проведения WorldSkills'
        verbose_name_plural = 'Правила проведения WorldSkills'

""" Компетенция """
class CompetentionModel(models.Model):
    title = models.CharField(verbose_name='Наименование компетенции', max_length=100)
    # description = models.TextField(verbose_name='Описание компетенции', blank=True, default='')

    class Meta:
        verbose_name = 'Компетенция'
        verbose_name_plural = 'Компетенция'
    
    def __str__(self) -> str:
        return self.title

""" Документация к компетенции """
class CompetentionDocumentationModel(models.Model):
    title = models.CharField(max_length=255, default='')
    file1 = models.FileField(verbose_name='Файл', upload_to="uploads/worldskills/documentations/")
    competention = models.ForeignKey(CompetentionModel, related_name='Компетенция', on_delete=models.CASCADE)
    public = models.BooleanField(verbose_name='Опубликовать', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Документация к компетенции'
        verbose_name_plural = 'Документация к компетенции'
    
    def __str__(self) -> str:
        return self.competention.title