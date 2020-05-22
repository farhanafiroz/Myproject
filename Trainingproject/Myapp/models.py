from django.db import models

# Create your models here.
# name of table-->model(class)
# fields of my table--> attributes of class


class Signup(models.Model):
    username = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Session(models.Model):
    session=models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.session
class Student(models.Model):
    name=models.CharField(max_length=20, unique=False)
    session=models.ForeignKey("session", on_delete=models.PROTECT)

    def __str__(self):
        return self.name