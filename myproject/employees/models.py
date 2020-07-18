from django.db import models

# Create your models here.

class employee(models.Model):
    firstname=models.CharField(max_length=70, blank=False, default='')
    lastname=models.CharField(max_length=70, blank=False, default='')
    ispermanent=models.BooleanField(default=False)