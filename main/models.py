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