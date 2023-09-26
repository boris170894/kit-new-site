from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name ='index'),
    
    # TODO: About Section
    path('college-history/', views.college_history, name = 'college-history'),
    path('documents/', views.documents, name = 'documents'),
    
    
    # TODO: Information 
    path('abiturients/', views.abiturients, name = 'abiturients'),  
    path('students/schedule', views.call_pair_schedule, name = 'call_pair_schedule'),  
    path('students/academic-process', views.academic_process_schedule, name = 'academic_process_schedule'),  
    path('students/student-events', views.student_events, name = 'student_events'),  
    path('students/student-events/<int:pk>', views.student_event_one, name = 'student_event_one'),  
    
    # TODO: State
    path('state-symbols/', views.state_symbols, name = 'state_symbols'),
    
]
