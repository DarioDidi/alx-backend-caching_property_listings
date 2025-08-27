from django.db import models

# Create your models here.
'''
Create a Property model in properties/models.py with fields:

    title (CharField, max_length=200)
    description (TextField)
    price (DecimalField, )
    location (CharField, max_length=100)
    created_at (DateTimeField, autonowadd=True)
'''


class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
