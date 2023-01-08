from django.contrib import admin
from crudapp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
	list_display=['eid','ename','email','ephone_number','esalary','eaddress']

admin.site.register(Employee,EmployeeAdmin)