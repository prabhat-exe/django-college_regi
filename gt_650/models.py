from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.BigIntegerField()
    password=models.CharField(max_length=100)
    dt=models.CharField(max_length=10,null=True)
    # def __str__(self):
    #     return self.name