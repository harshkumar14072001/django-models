from django.db import models
from django.http import *

class post(models.Model):
     title=models.CharField(max_length=20)
     text=models.TextField()
     def __str__(self):
          return self.title
# Create your models here.
