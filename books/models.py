from django.db import models

# Create your models here.

# Book model
class Book(models.Model):
    title  = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    author  = models.CharField(max_length=200)
    publisher  = models.CharField(max_length=200)
    catgory  = models.CharField(max_length=200)
    pages = models.BigIntegerField()
    pubished_date = models.DateField()

    def __str__(self):
        return f"{self.title }   ({self.author})"


