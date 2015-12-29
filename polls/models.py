from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from  django import forms
# Create your models here.
@python_2_unicode_compatible
class Reporter(models.Model):
    full_name=models.CharField(max_length=200)
    def  __str__(self):
        return self.full_name

@python_2_unicode_compatible
class Artical(models.Model):
    pub_date=models.DateField()
    headline=models.CharField(max_length=200)
    content=models.TextField()
    def __str__(self):
        return self.headline
class raj(models.Model):
    rname=models.CharField(max_length=20)
    rollno=models.CharField(max_length=10)
    def __str__(self):
	    return self.rname
class choice(models.Model):
    shurt_sizes=(
	    ('S','small'),
	    ('M','medium'),
	    ('L','large')
    )
    shurt_size=models.CharField(max_length=1,choices=shurt_sizes)
    def __str__(self):
	    return self.shurt_size
class profit(models.Model):
    rno=models.CharField(max_length=15,primary_key=True)
    name=models.CharField(max_length=15)
    branchs=(
	    ('cse','cse'),
		('ece','ece'),
		('eee','eee'),
		('mec','mec')
	)
    branch=models.CharField(max_length=3,choices=branchs)
    phone=models.IntegerField(max_length=10)
    def __str__(self):
	    return self.rno
