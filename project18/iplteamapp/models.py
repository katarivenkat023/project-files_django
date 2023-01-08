from django.db import models

# Create your models here.
class iplteams(models.Model):
	names=models.CharField(max_length=50)
	def __str__(self):
		return self.names

class csk(models.Model):
	name=models.CharField(max_length=50)
	country=models.CharField(max_length=50)

class dc(models.Model):
	name=models.CharField(max_length=50)
	country=models.CharField(max_length=50)

class kp(models.Model):
	name=models.CharField(max_length=50)
	country=models.CharField(max_length=50)

class kkr(models.Model):
	name=models.CharField(max_length=50)
	country=models.CharField(max_length=50)

class mi(models.Model):
	name=models.CharField(max_length=50)
	country=models.CharField(max_length=50)

class rr(models.Model):
	name=models.CharField(max_length=50)
	country=models.CharField(max_length=50)

class rcb(models.Model):
	name=models.CharField(max_length=50)
	country=models.CharField(max_length=50)

class sh(models.Model):
	name=models.CharField(max_length=50)
	country=models.CharField(max_length=50)