from django.db import models
from .models import models

class staffs_models(models.Model):
    staffs_name = models.CharField(max_length=100, blank=True)
    

    def __str__():
        return self.staffs_name