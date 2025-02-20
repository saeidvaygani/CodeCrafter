from django.db import models
from .models import models 


class boards_models(models.Model):
    boards_name = models.CharField(max_length = 100, blank = True)
    boards_description = models.TextField( blank = True)
    boards_age = models.IntegerField(null = True, blank = True)
    boards_price = models.DecimalField(max_digits=6, decimal_places= 2, null = True, blank = True)
    boards_rating = models.FloatField(null = True, blank = True)
    boards_is_available = models.BooleanField(default = True, null = True, blank = True)
    
def __str__(self):
    return self.boards_name
    
