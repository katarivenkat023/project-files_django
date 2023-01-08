from django.db import models

# Create your models here.
class studentdetails(models.Model):
	name=models.CharField(max_length=50)
	age=models.IntegerField()
	address=models.CharField(max_length=50)
	joining_date=models.DateField()
	