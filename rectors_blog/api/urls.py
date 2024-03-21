from django.urls import path
from . import views

urlpatterns = [
    path('question-create/', views.question_create, name='question-create'),
]