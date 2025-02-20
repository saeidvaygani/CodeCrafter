from django.contrib import admin
from .models import staffs_models


class staffsAdmin(admin.ModelAdmin):
    list_display = ('staffs_name', 'staffs_age', 'staffs_price', 'staffs_rating', 'staffs_is_available' ,)
    list_filter =('staffs_rating', 'staffs_is_available',)
    search_fields = ('staffs_name',)


admin.site.register(staffs_models, staffsAdmin)


