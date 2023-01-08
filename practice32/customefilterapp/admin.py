from django.contrib import admin
from customefilterapp.models import employeedetails

# Register your models here.
class employeedetailsAdmin(admin.ModelAdmin):
	list_display=['emp_id','ename','age','address','technology']

admin.site.register(employeedetails,employeedetailsAdmin)