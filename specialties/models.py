from django.db import models

""" Специальности """
class SpecInfoModel(models.Model):

    spec_name = models.CharField(verbose_name='Специальность', max_length=200)
    spec_info = models.TextField(verbose_name='Описание')
    spec_img = models.ImageField(verbose_name='Изображение', upload_to = 'upload/specs', blank = True)

    def __str__(self):
        return self.spec_name

    class Meta:
        verbose_name = 'Специальности'
        verbose_name_plural = 'Специальности'
