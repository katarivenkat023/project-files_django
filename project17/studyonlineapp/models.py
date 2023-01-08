from django.db import models

# Create your models here.
class studyonline(models.Model):
	name=models.CharField(max_length=50)
	dob=models.DateField()
	studyonline_id=models.CharField(max_length=50)
	mail_id=models.EmailField()
	phone_number=models.CharField(max_length=50)
	branch=models.CharField(max_length=50)

	def __str__(self):
		return self.name
		