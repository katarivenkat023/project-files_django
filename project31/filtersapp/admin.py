from django.contrib import admin
from filtersapp.models import studentdetails

# Register your models here.
class AdminStudent(admin.ModelAdmin):
	list_display=['name','age','address','joining_date']
admin.site.register(studentdetails,AdminStudent)