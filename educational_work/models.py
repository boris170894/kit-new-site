from django.db import models
# from staff.models import 
from staff.models import PersonModel

"""
TODO: Воспитательная работа
"""

""" Общая информация """
class GeneralInformationFilesModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название файла')
    file = models.FileField(verbose_name='Файл', upload_to="uploads/educational-work/general-information/")
    is_public = models.BooleanField(verbose_name='Опубликовать', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Общая информация'
        verbose_name_plural = 'Общая информация'
    
    def __str__(self) -> str:
        return self.title
    
""" Кружки и секции """
class ClubsAndSectionsModel(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200) 
    about = models.TextField(verbose_name='О кружке или секции', blank=True, default='')
    teachers = models.ManyToManyField(PersonModel, related_name='Преподаватели', blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ' Кружки и секции'
        verbose_name_plural = ' Кружки и секции'
    
    def __str__(self) -> str:
        return self.title

""" Файлы  кружков и секций """
class ClubsAndSectionsDocumentsModel(models.Model):
    title = models.CharField(verbose_name='Название', max_length=400, blank=True)
    category = models.ForeignKey(ClubsAndSectionsModel, on_delete=models.CASCADE, related_name='Категория')
    file = models.FileField(verbose_name='Файл', upload_to="uploads/educational-work/clubs-and-sections/")
    public  = models.BooleanField(verbose_name='Опубликовать', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Файлы кружков и секций'
        verbose_name_plural = 'Файлы кружков и секций'

    def __str__(self) -> str:
        return self.title

""" Психологическая служба """
class PsychologicalServiceModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название файла')
    file = models.FileField(verbose_name='Файл', upload_to="uploads/educational-work/psychological-service/")
    is_public = models.BooleanField(verbose_name='Опубликовать', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Психологическая служба'
        verbose_name_plural = 'Психологическая служба'
    
    def __str__(self) -> str:
        return self.title


""" Молодежная политика """
class YouthPolicyModel(models.Model):
    documents = models.ManyToManyField('YouthPolicyFilesModel', related_name='Файлы', default=[], blank=True)
    images = models.ManyToManyField('YouthPolicyImagesModel', related_name='Изображения', default=[], blank=True)
    about = models.TextField(verbose_name="Описание", blank=True, null=True)

    is_public = models.BooleanField(verbose_name='Опубликовать', default=False)

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Молодежная политика'
        verbose_name_plural = 'Молодежная политика'

""" Молодежная политика Загрузка файлов """
class YouthPolicyFilesModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название файла')
    file = models.FileField(verbose_name='Файл', upload_to="uploads/educational-work/youth-policy/documents")
    is_public = models.BooleanField(verbose_name='Опубликовать', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Молодежная политика Файлы'
        verbose_name_plural = 'Молодежная политика Файлы'

    def __str__(self) -> str:
        return self.title


""" Молодежная политика Загрузка фото """
class YouthPolicyImagesModel(models.Model):
    file = models.ImageField(verbose_name='Изображение', upload_to="uploads/educational-work/youth-policy/images")
    is_public = models.BooleanField(verbose_name='Опубликовать', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Молодежная политика Фото'
        verbose_name_plural = 'Молодежная политика Фото'