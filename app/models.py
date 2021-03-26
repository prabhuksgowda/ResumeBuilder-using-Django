from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Details(models.Model):
    name = models.CharField(max_length=100 )
    email = models.CharField(max_length=100 )
    mobile = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    carrearobject = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='flash')
    def __str__(self):
        return self.name

class Education(models.Model):
    collagename = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    yearofpass = models.CharField(max_length=4)
    programinglang = models.CharField(max_length=250)
    frontendlng = models.CharField(max_length=250, null=True)
    framework = models.CharField(max_length=250, null=True)
    cgpa = models.CharField(max_length=250) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)   
    def __str__(self):
        return self.collagename

class Project(models.Model):
    projecttitle = models.CharField(max_length=250, )
    prodescrip = models.TextField( )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.projecttitle

class Personaldetails(models.Model):
    dob = models.CharField(max_length=100 )
    gender = models.CharField(max_length=100 )
    nationality = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    strength = models.CharField(max_length=100,null=True )
    hobbies = models.CharField(max_length=100,null=True )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.fathername

