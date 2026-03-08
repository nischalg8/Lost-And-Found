from django.db import models
from django.conf import settings

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_found = models.DateField()
    location = models.CharField(max_length=100)
    found_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name