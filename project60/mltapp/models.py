from django.db import models

# Create your models here.

class Parent1(models.Model):
	name = models.CharField( max_length=50)
	dob = models.CharField(max_length=50)

class Parent2(models.Model):
	eno = models.IntegerField()
	esalary = models.IntegerField()
	
class Child(Parent1,Parent2):
	no_of_projects = models.IntegerField()
	