from django.db import models


# Create your models here.
# name of table-->model(class)
# fields of my table--> attributes of class

class Signup(models.Model):
    username = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
