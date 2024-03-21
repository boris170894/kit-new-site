from django.db import models

""" Контакты """
class CollegeContactModel(models.Model):
    addr = models.CharField(verbose_name='Адрес', max_length=300, blank=True)
    e_mail = models.CharField(verbose_name='e-mail', max_length=20, blank=True)
    tel = models.CharField(verbose_name='Телефон', max_length=20, blank=True)
    priem_com = models.CharField(verbose_name='Приёмная комиссия', max_length=20, blank=True)
    wats = models.CharField(verbose_name='Watsapp', max_length=20, blank=True)
    workSchedule = models.CharField(verbose_name='График работы', max_length=200, blank=True)

    public = models.BooleanField(verbose_name='Опубликовать', default=False)

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
