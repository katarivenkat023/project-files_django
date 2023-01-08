from django.contrib import admin
from adminapp.models import student
# Register your models here.
class Adminstudent(admin.ModelAdmin):
	list_display=['name','roll_no','address']

admin.site.register(student,Adminstudent)