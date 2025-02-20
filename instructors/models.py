from django.db import models
from .models import models


class instructor_models(models.Model):
    instructore_name = models.CharField(max_length=50, blank = True)
    
    def __str__(self):
        return self.instructore_name