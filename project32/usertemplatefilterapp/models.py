from django.db import models

# Create your models here.
class UserTemplateFilter(models.Model):

    name = models.CharField(max_length=20)
    technology = models.CharField(max_length=50)
    trainer = models.CharField(max_length=50)
    