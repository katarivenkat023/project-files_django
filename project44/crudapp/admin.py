from django.contrib import admin
from crudapp.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    '''
        Admin View for Employee
    '''
    list_display = ['id','eno','ename','esalary','eaddress']
   

admin.site.register(Employee, EmployeeAdmin) 