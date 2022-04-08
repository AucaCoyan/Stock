from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0, message='This number cannot be less than 0')])
    rented = models.IntegerField(
        validators=[MinValueValidator(0, message='This number cannot be less than 0')])
    
    def __str__(self):
        return self.name
