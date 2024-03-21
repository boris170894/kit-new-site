from django.urls import path
from .views import announcement

urlpatterns = [
    path('', announcement, name='announcement'),
]