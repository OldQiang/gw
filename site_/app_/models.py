from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)
    password = models.CharField(null=True, blank=True, max_length=100)

