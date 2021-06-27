from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    employee_name =  models.CharField(max_length=50)
    employee_Position =  models.CharField(max_length=50)
    employee_discription =  models.CharField(max_length=100)
    employee_twitter = models.URLField(null=True,max_length=50)
    employee_facebook = models.URLField(null=True,max_length=50)
    employee_linkedin = models.URLField(null=True,max_length=50)
    employee_insta = models.URLField(null=True,max_length=50)
    employee_image = models.FileField(null=True)
    def __str__(self):
        return self.employee_name

class customer(models.Model):
    name =  models.CharField(max_length=50)
    profression =  models.CharField(max_length=50)
    discription =  models.TextField(max_length=1500)
    image = models.FileField(null=True)
    def __str__(self):
        return self.name

  

class client_tail(models.Model):
    name =  models.CharField(max_length=50)
    paragraph =  models.CharField(max_length=90)
    image = models.FileField(null=True)
    facebook = models.URLField(null=True,max_length=90)
    instagram = models.URLField(null=True,max_length=90)
    website = models.URLField(null=True,max_length=90)
    twitter = models.URLField(null=True,max_length=90)
    def __str__(self):
        return self.name
    
class SERVICES(models.Model):
    service_name = models.CharField(max_length=50)
    service_paragraph = models.TextField(max_length=1000)
    service_logo = models.FileField(null=True)
    def __str__(self):
        return self.service_name  
    

class Articles(models.Model):
    name =  models.TextField(max_length=150)
    image = models.FileField(null=True)
    discription =  models.TextField(max_length=800)
    category=  models.CharField(max_length=90)
    date =  models.DateField(null=True)
    def __str__(self):
        return self.name

class story_of_vistaar(models.Model):
    story =  models.CharField(max_length=3000)
    

    
class Demo_image(models.Model):

    image = models.FileField(null=True)
    