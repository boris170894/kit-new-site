from django.db import models


class PositionModel(models.Model):
    position_name = models.CharField(verbose_name='Должность', max_length=200)

    def __str__(self):
        return self.position_name
    
    class Meta:
        verbose_name = 'Справочник должностей'
        verbose_name_plural = 'Справочник должностей'

class DirectorModel(models.Model):
    fio = models.CharField(verbose_name='ФИО', max_length=100)
    foto = models.ImageField(upload_to='upload/staff', verbose_name='Фото', blank=True)
    position = models.ForeignKey('PositionModel', on_delete=models.PROTECT, verbose_name='Должность')
    info = models.TextField(verbose_name='Информация', blank=True)
    is_working = models.BooleanField(default=False, verbose_name='Статус работы')
    slug = models.SlugField(verbose_name='URL', max_length=100, unique=True)

    def __str__(self):
        return self.fio
    
    class Meta:
        verbose_name = 'Директор'
        verbose_name_plural = 'Директор'


class DepDirectorModel(models.Model):
    fio = models.CharField(verbose_name='ФИО', max_length=100)
    foto = models.ImageField(upload_to='upload/staff', verbose_name='Фото', blank=True)
    position = models.ForeignKey('PositionModel', on_delete=models.PROTECT, verbose_name='Должность')
    info = models.TextField(verbose_name='Информация', blank=True)
    is_working = models.BooleanField(default=False, verbose_name='Статус работы')
    slug = models.SlugField(verbose_name='URL', max_length=100, unique=True)

    def __str__(self):
        return self.fio
    
    class Meta:
        verbose_name = 'Заместители директора'
        verbose_name_plural = 'Заместители директора'


class DepHeadModel(models.Model):
    fio = models.CharField(verbose_name='ФИО', max_length=100)
    foto = models.ImageField(upload_to='upload/staff', verbose_name='Фото', blank=True)
    position = models.ForeignKey('PositionModel', on_delete=models.PROTECT, verbose_name='Должность')
    info = models.TextField(verbose_name='Информация', blank=True)
    is_working = models.BooleanField(default=False, verbose_name='Статус работы')
    slug = models.SlugField(verbose_name='URL', max_length=100, unique=True)

    def __str__(self):
        return self.fio
    
    class Meta:
        verbose_name = 'Заведующий отделением'
        verbose_name_plural = 'Заведующий отделением'


class CmcOBModel(models.Model):
    fio = models.CharField(verbose_name='ФИО', max_length=100)
    foto = models.ImageField(upload_to='upload/staff', verbose_name='Фото', blank=True)
    position = models.ForeignKey('PositionModel', on_delete=models.PROTECT, verbose_name='Должность')
    info = models.TextField(verbose_name='Информация', blank=True)
    is_working = models.BooleanField(default=False, verbose_name='Статус работы')
    slug = models.SlugField(verbose_name='URL', max_length=100, unique=True)

    def __str__(self):
        return self.fio
    
    class Meta:
        verbose_name = 'ЦМК общеодразовательных дисциплин'
        verbose_name_plural = 'ЦМК общеодразовательных дисциплин'


class CmcLangModel(models.Model):
    fio = models.CharField(verbose_name='ФИО', max_length=100)
    foto = models.ImageField(upload_to='upload/staff', verbose_name='Фото', blank=True)
    position = models.ForeignKey('PositionModel', on_delete=models.PROTECT, verbose_name='Должность')
    info = models.TextField(verbose_name='Информация', blank=True)
    is_working = models.BooleanField(default=False, verbose_name='Статус работы')
    slug = models.SlugField(verbose_name='URL', max_length=100, unique=True)

    def __str__(self):
        return self.fio
    
    class Meta:
        verbose_name = 'ЦМК языковых дисциплин'
        verbose_name_plural = 'ЦМК языковых дисциплин'


class CmcELModel(models.Model):
    fio = models.CharField(verbose_name='ФИО', max_length=100)
    foto = models.ImageField(upload_to='upload/staff', verbose_name='Фото', blank=True)
    position = models.ForeignKey('PositionModel', on_delete=models.PROTECT, verbose_name='Должность')
    info = models.TextField(verbose_name='Информация', blank=True)
    is_working = models.BooleanField(default=False, verbose_name='Статус работы')
    slug = models.SlugField(verbose_name='URL', max_length=100, unique=True)

    def __str__(self):
        return self.fio
    
    class Meta:
        verbose_name = 'ЦМК электротехнических и экономических дисциплин'
        verbose_name_plural = 'ЦМК электротехнических и экономических дисциплин'

class CmcITModel(models.Model):
    fio = models.CharField(verbose_name='ФИО', max_length=100)
    foto = models.ImageField(upload_to='upload/staff', verbose_name='Фото', blank=True)
    position = models.ForeignKey('PositionModel', on_delete=models.PROTECT, verbose_name='Должность')
    info = models.TextField(verbose_name='Информация', blank=True)
    is_working = models.BooleanField(default=False, verbose_name='Статус работы')
    slug = models.SlugField(verbose_name='URL', max_length=100, unique=True)

    def __str__(self):
        return self.fio
    
    class Meta:
        verbose_name = 'ЦМК информационных дисциплин'
        verbose_name_plural = 'ЦМК информационных дисциплин'


class CmcFIZModel(models.Model):
    fio = models.CharField(verbose_name='ФИО', max_length=100)
    foto = models.ImageField(upload_to='upload/staff', verbose_name='Фото', blank=True)
    position = models.ForeignKey('PositionModel', on_delete=models.PROTECT, verbose_name='Должность')
    info = models.TextField(verbose_name='Информация', blank=True)
    is_working = models.BooleanField(default=False, verbose_name='Статус работы')
    slug = models.SlugField(verbose_name='URL', max_length=100, unique=True)

    def __str__(self):
        return self.fio
    
    class Meta:
        verbose_name = 'ЦМК физической культуры и НВП'
        verbose_name_plural = 'ЦМК физической культуры и НВП'