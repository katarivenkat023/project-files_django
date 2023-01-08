from django.db import models

# Create your models here.
class employeedetails(models.Model):
	emp_id=models.IntegerField()
	ename=models.CharField(max_length=50)
	age=models.IntegerField()
	address=models.CharField(max_length=50)
	technology=models.CharField(max_length=50)