from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    description = models.TextField()
