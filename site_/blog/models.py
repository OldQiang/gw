from django.db import models


# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=256)
    date = models.DateTimeField(max_length=256)