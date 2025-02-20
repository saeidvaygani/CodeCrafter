from django.db import models
from .models import models

class staffs_models(models.Model):
    
    staffs_name = models.CharField(max_length=100, blank=True)
    staffs_descriptions = models.TextField(blank = True)
    staffs_age = models.IntegerField( null = True, blank = True)
    staffs_price = models.DecimalField(max_digits = 6, decimal_places=2, null = True, blank = True)
    staffs_rating = models.FloatField(null = True, blank = True)
    staffs_is_available = models.BooleanField(default = True, null = True, blank = True)

    def __str__(self):
        return self.staffs_name