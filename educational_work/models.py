from django.db import models

""" Общая информация файл и название файла"""
class GeneralInformationFilesModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название файла')
    file = models.FileField(verbose_name='Файл', upload_to="uploads/educational_work/general_information/")
    is_public = models.BooleanField(default=True, verbose_name='Статус файла')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Файлы для страницы общей информации'
        verbose_name_plural = 'Файлы для страницы  общей информации'
    
    def __str__(self) -> str:
        return self.title