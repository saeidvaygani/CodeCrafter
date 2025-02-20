from django.contrib import admin
from .models import students_models


class studentsAdmin(admin.ModelAdmin):
    list_display = ('students_name','students_age','students_price', 'students_rating', 'students_is_available',)
    list_filter = ('students_rating', 'students_is_available')
    search_fields = ('students_name', )





admin.site.register(students_models,studentsAdmin)


