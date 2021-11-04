from django.db import models

# Create your models here.


class privateJobs(models.Model):

    name = models.CharField(max_length=100) 
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price1 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    link = models.URLField(max_length=225, null=True)

class privateJobs1(models.Model):
    
    name = models.CharField(max_length=100) 
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price1 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    link = models.URLField(max_length=225, null=True)

class govJobs1(models.Model):
     
    name = models.CharField(max_length=100) 
    sector = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price1 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    link = models.URLField(max_length=225, null=True)

    