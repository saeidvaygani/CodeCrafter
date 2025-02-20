from django.urls import path
from .views import InstructorsViews

urlpatterns = [
    path('', InstructorsViews, name='InstructorsViews')
]
