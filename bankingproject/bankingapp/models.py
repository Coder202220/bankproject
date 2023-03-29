from django.db import models

# Create your models here.

class Apply(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=250)
    phoneno=models.PositiveBigIntegerField()
    mailid=models.EmailField()
    address=models.TextField()
    district=models.IntegerField()
    branch=models.CharField(max_length=250)
    account_type=models.CharField(max_length=250)
    material=models.TextField(null=True)