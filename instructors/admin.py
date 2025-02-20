from django.contrib import admin
from .models import instructors_models


class InstructorsAdmin(admin.ModelAdmin):
    list_display = ('instructors_name','instructors_age','instructors_price','instructors_rating','instructors_is_available',)
    list_filter = ('instructors_rating','instructors_is_available',)
    search_fields = ('instructors_name',)
    
admin.site.register(instructors_models,InstructorsAdmin)

