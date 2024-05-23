from django.db import models


""" Объявления """
class AnnouncementModel(models.Model):
    about = models.TextField(verbose_name="Описание", blank=True, null=True)
    video = models.FileField("Видео", upload_to='uploads/announcement/videos', blank=True)

    is_public = models.BooleanField(verbose_name='Опубликовать', default=False)

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Объявления'
        verbose_name_plural = 'Объявления'

""" Объявления, Загрузка файлов """
class AnnouncementFilesModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название файла')
    file = models.FileField(verbose_name='Файл', upload_to="uploads/announcement/documents")

    is_public = models.BooleanField(verbose_name='Опубликовать', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Объявления, Файлы'
        verbose_name_plural = 'Объявления, Файлы'

    def __str__(self) -> str:
        return self.title

""" Объявления, Загрузка фото """
class AnnouncementImagesModel(models.Model):
    file = models.ImageField(verbose_name='Изображение', upload_to="uploads/announcement/images")

    is_public = models.BooleanField(verbose_name='Опубликовать', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Объявления, Фото'
        verbose_name_plural = 'Объявления, Фото'

""" Объявления, Вакансии """
class AnnouncementVacanciesModel(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)
    salary = models.CharField(max_length=200, verbose_name='Зарплата', blank=True)
    experience_years = models.CharField(max_length=200, verbose_name='Количество лет опыта', blank=True)
    file = models.FileField(verbose_name='Файл', upload_to="uploads/announcement/vacancies", blank=True, null=True)

    is_public = models.BooleanField(default=False, verbose_name='Опубликовать')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Объявления, вакансии'
        verbose_name_plural = 'Объявления, вакансии'

    def __str__(self):
        return self.title
