from django.db import models


""" Группа """
class GroupModel(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название группы')
    curator = models.ForeignKey('PersonModel', on_delete=models.PROTECT, verbose_name='Куратор группы')
    
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группа'
    
    def __str__(self) -> str:
        return self.name

""" ЦМК """
class CMCModel(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    
    class Meta:
        verbose_name = 'ЦМК дисциплины и другие'
        verbose_name_plural = 'ЦМК дисциплины и другие'

    def __str__(self):
        return self.title

""" Должность """
class PositionModel(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    cmc = models.ForeignKey(CMCModel, on_delete=models.PROTECT, )
    
    class Meta:
        verbose_name = 'Справочник должностей'
        verbose_name_plural = 'Справочник должностей'

    def __str__(self) -> str:
        return self.title

""" Персонал """
class PersonModel(models.Model):
#    CMC = [
#         ('Директор', 'Директор'),
#         ('Заместители директора', 'Заместители директора'),
#         ('Заведующий отделением', 'Заведующий отделением'),
#         ('ЦМК общеодразовательных дисциплин', 'ЦМК общеодразовательных дисциплин'),
#         ('ЦМК языковых дисциплин', 'ЦМК языковых дисциплин'),
#         ('ЦМК электротехнических и экономических дисциплин', 'ЦМК электротехнических и экономических дисциплин'),
#         ('ЦМК информационных дисциплин', 'ЦМК информационных дисциплин'),
#         ('ЦМК физической культуры и НВП', 'ЦМК физической культуры и НВП'),
#     ] 
    fio = models.CharField(verbose_name='ФИО', max_length=100)
    slug = models.SlugField(verbose_name='URL', max_length=100, unique=True)
    foto = models.ImageField(upload_to='upload/about-college/staff', verbose_name='Фото', blank=True)

    position = models.ForeignKey(PositionModel, on_delete=models.PROTECT, verbose_name='Должность', blank=True, default='', null=True)
    cmc = models.ForeignKey(CMCModel, on_delete=models.PROTECT, verbose_name='ЦМК')

    info = models.TextField(verbose_name='Информация', blank=True)
    is_working = models.BooleanField(default=False, verbose_name='Статус работы')

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'

    def __str__(self) -> str:
        return self.fio