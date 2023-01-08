from django.db import models

# Create your models here
class MovieInfo(models.Model):
	moviename=models.CharField(max_length=50)
	hero=models.CharField(max_length=50)
	heroine=models.CharField(max_length=50)
	releasedate=models.DateField()
	rating=models.IntegerField()
	director=models.CharField(max_length=50)
	timing=models.TimeField()
	language=models.CharField(max_length=50)