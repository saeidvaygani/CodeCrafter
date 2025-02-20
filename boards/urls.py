from django.urls import path 
from .views import BoardViews

urlpatterns = [
    path('', BoardViews, name = 'BoardViews')
]
