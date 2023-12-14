from django.db import models


class AntiCorruptionModel(models.Model):
    title1 = models.CharField(max_length=250, blank=True, verbose_name="Заголовок для 1 файла")
    file1 = models.FileField(verbose_name='Файл 1', upload_to="uploads/state/anti-corruption/", blank=True)

    title2 = models.CharField(max_length=250, blank=True, verbose_name="Заголовок для 2 файла")
    file2 = models.FileField(verbose_name='Файл 2', upload_to="uploads/state/anti-corruption/", blank=True)

    title3 = models.CharField(max_length=250, blank=True, verbose_name="Заголовок для 3 файла")
    file3 = models.FileField(verbose_name='Файл 3', upload_to="uploads/state/anti-corruption/", blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Противодействие коррупции'
        verbose_name_plural = 'Противодействие коррупции'