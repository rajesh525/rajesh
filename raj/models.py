from __future__ import unicode_literals

from django.db import models
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location='//raj//media//books')

# Create your models here.
class friends(models.Model):
    name=models.CharField(max_length=15)
    friend=models.CharField(max_length=30)
    def  __str__(self):
	    return self.name
class book(models.Model):
    name=models.CharField(max_length=15)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    photo=models.FileField(upload_to='media/books/')
    def __str__(self):
        return self.name