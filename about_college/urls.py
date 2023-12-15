from django.urls import path
from . import views

urlpatterns = [
    # TODO: About Section
    path('college-history/', views.about_college_history, name = 'college-history'),
    path('documents/', views.about_documents, name = 'documents'),

    path('board-of-trustees/', views.about_board_of_trustees, name = 'board-of-trustees'),
    path('pedagogical-council/', views.about_pedagogical_council, name = 'pedagogical-council'),
    path('industrial-council/', views.about_industrial_council, name = 'industrial-council'),
    
]
