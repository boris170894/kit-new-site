from django.db import models

""" Контакты """
class CollegeContactModel(models.Model):

    addr = models.CharField(verbose_name='Адрес', max_length=300)
    e_mail = models.CharField(verbose_name='e-mail', max_length=20)
    tel = models.CharField(verbose_name='Телефон', max_length=20)
    priem_com = models.CharField(verbose_name='Приёмная комиссия', max_length=20)
    wats = models.CharField(verbose_name='Watsapp', max_length=20)
    
    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self) -> str:
        return("Информация")

""" Расписание звонков и основное расписание """
class CallPairScheduleModel(models.Model):
    call_schedule_1_pair = models.CharField(max_length=20, verbose_name="1 пара", default='')
    call_schedule_2_pair = models.CharField(max_length=20, verbose_name="2 пара", default='')
    call_schedule_3_pair = models.CharField(max_length=20, verbose_name="3 пара", default='')
    call_schedule_4_pair = models.CharField(max_length=20, verbose_name="4 пара", default='')
    call_schedule_5_pair = models.CharField(max_length=20, verbose_name="5 пара", default='')
    call_schedule_6_pair = models.CharField(max_length=20, verbose_name="6 пара", default='')
    call_schedule_7_pair = models.CharField(max_length=20, verbose_name="7 пара", default='')
    
    course_1_schedule = models.FileField(upload_to="uploads/information/schedule",
                                     verbose_name="Расписание пар 1 курс", 
                                     blank=True)
    course_2_schedule = models.FileField(upload_to="uploads/information/schedule",
                                     verbose_name="Расписание пар 2 курс", 
                                     blank=True)
    course_3_schedule = models.FileField(upload_to="uploads/information/schedule",
                                     verbose_name="Расписание пар 3 курс", 
                                     blank=True)
    course_4_schedule = models.FileField(upload_to="uploads/information/schedule",
                                     verbose_name="Расписание пар 4 курс", 
                                     blank=True)
    
    class Meta:
        verbose_name = 'Расписание звонков и расписание пар'
        verbose_name_plural = 'Расписание звонков и расписание пар'
        
""" График Учебного процесса """
class AcademicProcessScheduleModel(models.Model):
    file =  models.FileField(upload_to="uploads/information/year-schedule",
                                     verbose_name="График Учебного процесса", 
                                     blank=True)

    class Meta:
        verbose_name = 'График Учебного процесса'
        verbose_name_plural = 'График Учебного процесса'

""" События для студентов """
class StudentEventModel(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=200)
    description = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(verbose_name='Изображение',upload_to="uploads/information/student/events", blank=True)

    start_date = models.DateTimeField(verbose_name='Дата начала', blank=True)
    end_date = models.DateTimeField(verbose_name='Дата конца', blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'События для студента'
        verbose_name_plural = 'События для студента'
    
""" Категории методических рекомендаций """
class MetodicRecomendationsCategoryModel(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=200)    

    is_for_student = models.BooleanField(verbose_name='Это для студентов', default=False)
    is_for_teacher = models.BooleanField(verbose_name='Это для преподавателей', default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Категории методических рекомендаций'
        verbose_name_plural = 'Категории методических рекомендаций'
    
    def __str__(self) -> str:
        return self.title

""" Файлы методических рекомендаций """
class MetodicRecomendationsDocumentModel(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=400, blank=True)
    category = models.ForeignKey(MetodicRecomendationsCategoryModel, on_delete=models.CASCADE, related_name='Категория')
    file = models.FileField(verbose_name='Файл', upload_to="uploads/information/metodic-recomendations/")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Файлы методических рекомендаций'
        verbose_name_plural = 'Файлы методических рекомендаций'

    def __str__(self) -> str:
        return self.title
    
""" Финансовая отчетность """
class FinancialStatementsModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название файла')
    file = models.FileField(verbose_name='Файл', upload_to="uploads/information/financial-statements/")
    is_public = models.BooleanField(verbose_name='Опубликовать', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Финансовая отчетность'
        verbose_name_plural = 'Финансовая отчетность'
    
    def __str__(self) -> str:
        return self.title
    
""" Перечень необходимых документов """
class CollegeDocsModel(models.Model):
    title = models.CharField(verbose_name="Название документа", max_length=500)
    is_public = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Документы для поступления в колледж'
        verbose_name_plural = 'Документы для поступления в колледж'
    
    def __str__(self) -> str:
        return self.title
    
""" Основные преимущества нашего колледжа """
class MainAdvantagesOfOurCollegeModel(models.Model):
    title = models.CharField(verbose_name="Название документа", max_length=500)
    is_public = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Основные преимущества нашего колледжа'
        verbose_name_plural = 'Основные преимущества нашего колледжа'
    
    def __str__(self) -> str:
        return self.title


""" Библиотека """
class LibraryModel(models.Model):
    text = models.TextField(verbose_name="Описание", blank=True)
    slider_images = models.ManyToManyField('LibrarySliderImageModel', default=None, blank=True, verbose_name='Изображения')
    slider_files = models.ManyToManyField('LibraryFilesModel', default=None, blank=True, verbose_name='Файлы')

    is_public = models.BooleanField(verbose_name='Опубликовать', default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Библиотека'
        verbose_name_plural = 'Библиотека'

""" Библиотека, изображения для слайдера """
class LibrarySliderImageModel(models.Model):
    image = models.ImageField(verbose_name='Изображение', upload_to="uploads/information/library/slider")

    is_public = models.BooleanField(verbose_name='Опубликовать', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Библиотека, изображения для слайдера'
        verbose_name_plural = 'Библиотека, изображения для слайдера'

""" Библиотека, файлы """
class LibraryFilesModel(models.Model):
    title = models.CharField(verbose_name='Название файла', max_length=250, )
    file = models.FileField(verbose_name='Файл', upload_to="uploads/information/library/files")

    is_public = models.BooleanField(verbose_name='Опубликовать', default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Библиотека, файлы'
        verbose_name_plural = 'Библиотека, файлы'

    def __str__(self) -> str:
        return self.title


""" Общежитие """
class DormitoryModel(models.Model):
    documents = models.ManyToManyField('DormitoryFilesModel', related_name='Файлы')
    images = models.ManyToManyField('DormitoryImagesModel', related_name='Изображения')
    about = models.TextField(verbose_name="Описание", blank=True, null=True)
    contact_email = models.ManyToManyField('DormitoryContactsEmailModel', verbose_name="Почты", default=[], blank=True)
    contact_phone = models.ManyToManyField('DormitoryContactsPhoneModel', verbose_name="Телефоны", default=[],
                                           blank=True)

    is_public = models.BooleanField(verbose_name='Опубликовать', default=False)

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Общежитие'
        verbose_name_plural = 'Общежитие'


""" Контакты общежития, email """
class DormitoryContactsEmailModel(models.Model):
    email = models.EmailField(verbose_name='Почта', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Email общежития'
        verbose_name_plural = 'Email общежития'

    def __str__(self) -> str:
        return self.email


""" Контакты общежития, телефон """
class DormitoryContactsPhoneModel(models.Model):
    phone = models.CharField(verbose_name='Номер телефона', max_length=20, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Телефон общежития'
        verbose_name_plural = 'Телефон общежития'

    def __str__(self) -> str:
        return self.phone


""" Общежитие Загрузка файлов """
class DormitoryFilesModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название файла')
    file = models.FileField(verbose_name='Файл', upload_to="uploads/educational-work/dormitory/documents")
    is_public = models.BooleanField(verbose_name='Опубликовать', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Общежитие Файлы'
        verbose_name_plural = 'Общежитие Файлы'

    def __str__(self) -> str:
        return self.title


""" Общежитие Загрузка фото """
class DormitoryImagesModel(models.Model):
    file = models.ImageField(verbose_name='Изображение', upload_to="uploads/educational-work/dormitory/images")
    is_public = models.BooleanField(verbose_name='Опубликовать', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Общежитие Фото'
        verbose_name_plural = 'Общежитие Фото'

""" Наш профсоюз """
class OurUnionModel(models.Model):
    documents = models.ManyToManyField('OurUnionFilesModel', related_name='Файлы', default=[], blank=True)
    images = models.ManyToManyField('OurUnionImagesModel', related_name='Изображения', default=[], blank=True)
    about = models.TextField(verbose_name="Описание", blank=True, null=True)

    is_public = models.BooleanField(verbose_name='Опубликовать', default=False)

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Наш профсоюз'
        verbose_name_plural = 'Наш профсоюз'

""" Наш профсоюз Загрузка файлов """
class OurUnionFilesModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название файла')
    file = models.FileField(verbose_name='Файл', upload_to="uploads/information/our-union/documents")
    is_public = models.BooleanField(verbose_name='Опубликовать', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Наш профсоюз Файлы'
        verbose_name_plural = 'Наш профсоюз Файлы'

    def __str__(self) -> str:
        return self.title


""" Наш профсоюз Загрузка фото """
class OurUnionImagesModel(models.Model):
    file = models.ImageField(verbose_name='Изображение', upload_to="uploads/information/our-union/images")
    is_public = models.BooleanField(verbose_name='Опубликовать', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Наш профсоюз Фото'
        verbose_name_plural = 'Наш профсоюз Фото'