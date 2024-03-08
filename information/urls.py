from django.urls import path
from . import views

urlpatterns = [
    # TODO: Information 
    path('abiturients/', views.abiturients, name = 'abiturients'),
    
    # * For Students  
    path('students/schedule/', views.call_pair_schedule_students, name = 'call_pair_schedule'),  
    path('students/guidelines/', views.guidelines_students, name = 'guidelines_students'),  
    path('students/academic-process/', views.academic_process_schedule_students, name = 'academic_process_schedule'),  
    path('students/student-events/', views.student_events, name = 'student_events'),  
    path('students/student-events/<int:pk>/', views.student_event_one, name = 'student_event_one'),  
    
    # * Teachers 
    path('teachers/schedule/', views.call_pair_schedule_teachers, name = 'call_pair_schedule_teachers'),  
    path('teachers/guidelines/', views.academic_process_schedule_teachers, name = 'academic_process_schedule_teachers'),  
    path('teachers/academic-process/', views.guidelines_teachers, name = 'guidelines_teachers'),  

    path('financial-statements/', views.financial_statement, name='financial_statement'),

    path('dormitory/', views.dormitory, name='dormitory'),
    path('library/', views.library, name='library'),

]
