from django.urls import path 
from .views import StudentsViews

urlpatterns = [
    path('',StudentsViews, name='StudentsViews')
]
