from django.db import models
from django.core.validators import MinLengthValidator


""" Блог Ректора Главная информация """
class RectorsBlogMainInfoModel(models.Model):
    fio = models.CharField(max_length=400, verbose_name='ФИО', blank=True)
    info = models.TextField(verbose_name='Приветсвие', blank=True)
    image = models.ImageField(upload_to="uploads/rectors-blog/info", verbose_name="Фото", blank=True)
    appointment_schedule = models.CharField(max_length=300, verbose_name="График приема", blank=True)
    cabinet = models.CharField(max_length=100, verbose_name="Кабинет", blank=True)
    reception = models.CharField(max_length=100, verbose_name="Приемная", blank=True)
    email = models.EmailField(max_length=100, verbose_name="Email", blank=True)

    is_public = models.BooleanField(verbose_name='Опубликовать', default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Блог Ректора Главная информация'
        verbose_name_plural = 'Блог Ректора Главная информация'

    def __str__(self):
        return self.fio


""" Блог Ректора Вопрос - Ответ """
class RectorsBlogQuestionAnswerModel(models.Model):
    firstName = models.CharField(max_length=100, verbose_name="Имя", validators=[MinLengthValidator(3)])
    lastName = models.CharField(max_length=100, verbose_name="Фамилия", validators=[MinLengthValidator(3)])
    email = models.EmailField(max_length=150, verbose_name="Email", validators=[MinLengthValidator(5)])

    question = models.CharField(max_length=800, verbose_name="Вопрос", validators=[MinLengthValidator(25)])
    answer = models.TextField(max_length=1000, verbose_name="Ответ", blank=True)

    is_public = models.BooleanField(verbose_name='Опубликовать', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Блог Ректора Вопрос - Ответ'
        verbose_name_plural = 'Блог Ректора Вопрос - Ответ'

    def __str__(self):
        return f'{self.firstName} {self.lastName} {self.question}'
