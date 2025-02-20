from django.urls import path 
from .views import StaffsViews 


urlpatterns = [
    path('', StaffsViews, name ='StaffsViews')
]
