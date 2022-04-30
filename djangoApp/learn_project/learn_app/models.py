
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User

class Kucharz(models.Model):
        
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    

class Potrawa(models.Model):
    name = models.CharField(max_length=255)
    smak = models.CharField(max_length=255)
    powi = models.ForeignKey(Kucharz,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
# Create your models here.
