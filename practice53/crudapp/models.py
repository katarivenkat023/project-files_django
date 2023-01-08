from django.db import models
from django.urls import reverse
# Create your models here.
class Employee(models.Model):
	eid=models.IntegerField()
	ename=models.CharField(max_length=50)
	email=models.EmailField()
	ephone_number=models.BigIntegerField()
	esalary=models.IntegerField()
	eaddress=models.CharField(max_length=50)
	
	def get_absolute_url(self):
		return reverse('detail',kwargs={'pk':self.pk})