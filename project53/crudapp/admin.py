from django.contrib import admin

from crudapp.models import Company
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    '''
        Admin View for Company
    '''
    list_display = ['name','location','ceo']
    

admin.site.register(Company, CompanyAdmin)