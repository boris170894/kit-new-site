from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name ='index'),
    
    # TODO: About Section
    path('college-history/', views.college_history, name = 'college-history'),
    path('documents/', views.documents, name = 'documents'),
    
    
    # TODO: Information 
    path('abiturients/', views.abiturients, name = 'abiturients'),  
    
    
    # TODO: State
    path('state-symbols/', views.state_symbols, name = 'state_symbols'),
    
]
