from django.db import models

# Create your models here.

class CountryName(models.Model):
    code    = models.CharField(primary_key=True, max_length=2)
    c_name  = models.CharField(max_length=30)

    def __str__(self):
        return self.c_name

class CountryName(models.Model):
    id
    year
    month
    
    code    = models.CharField(primary_key=True, max_length=2)

    def __str__(self):
        return self.c_name
