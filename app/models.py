from django.db import models

# Create your models here.
class Capital(models.Model):
    c_name=models.CharField(max_length=100,unique=True)
class Country(models.Model):
    c_name=models.ForeignKey(Capital,on_delete=models.CASCADE)
    dis_name=models.CharField(max_length=100)    
