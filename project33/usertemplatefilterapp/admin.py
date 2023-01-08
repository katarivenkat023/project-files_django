from django.contrib import admin
from usertemplatefilterapp.models import UserTemplateFilter
# Register your models here.
class UserTemplateFilterAdmin(admin.ModelAdmin):
    '''
        Admin View for UserTemplateFilter
    '''
    list_display = ['name','technology','trainer']
   

admin.site.register(UserTemplateFilter, UserTemplateFilterAdmin)