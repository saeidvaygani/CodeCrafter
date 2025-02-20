from django.db import models
from .models import models


class instructors_models(models.Model):
    instructors_name = models.CharField(max_length=50, blank = True)
    instructors_descriptions = models.TextField(blank = True)
    instructors_age = models.IntegerField( null = True, blank= True)
    instructors_price = models.DecimalField(max_digits=6, decimal_places=2, null = True, blank = True)
    instructors_rating = models.FloatField(null = True, blank = True)
    instructors_is_available = models.BooleanField(default = True, null = True, blank = True)
    
    
    def __str__(self):
        return self.instructors_name