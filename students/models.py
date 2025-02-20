from django.db import models
from .models import models 

class students_models(models.Model):

    students_name = models.CharField(max_length = 100, blank = True)
    students_description = models.TextField(blank = True)
    students_age = models.IntegerField( null= True, blank = True)
    students_price = models.DecimalField(max_digits = 6, decimal_places = 2, null = True, blank = True)
    students_rating = models.FloatField(null = True, blank = True)
    students_is_available = models.BooleanField( default = True, null = True, blank = True)
    
    
    def __str__(self):
        return self.students_name
    