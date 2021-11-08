from django.db import models

# Create your models here.
class Employee(models.Model):
    empId = models.IntegerField()
    empname = models.CharField(max_length=100)
    empemail = models.EmailField(max_length=100)
    emppass = models.CharField(max_length=100)
    empmobile = models.CharField(max_length=100)
    empaddress = models.CharField(max_length=100)

