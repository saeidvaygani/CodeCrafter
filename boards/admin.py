from django.contrib import admin
from .models import boards_models

class boards_Admin(admin.ModelAdmin):
    list_display = ('boards_name', 'boards_age', 'boards_price', 'boards_rating', 'boards_is_available',)
    list_filter = ('boards_rating','boards_is_available',)
    search_fields = ('boards_name',)
    

admin.site.register(boards_models, boards_Admin)

