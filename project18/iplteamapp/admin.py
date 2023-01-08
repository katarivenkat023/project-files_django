from django.contrib import admin
from iplteamapp.models import iplteams,csk,dc,kp,kkr,mi,rr,rcb,sh
# Register your models here.

admin.site.register(iplteams)

class Admincsk(admin.ModelAdmin):
	list_display=['name','country']
admin.site.register(csk,Admincsk)
class Admindc(admin.ModelAdmin):
	list_display=['name','country']
admin.site.register(dc,Admindc)
class Adminkp(admin.ModelAdmin):
	list_display=['name','country']
admin.site.register(kp,Adminkp)
class Adminkkr(admin.ModelAdmin):
	list_display=['name','country']
admin.site.register(kkr,Adminkkr)
class Adminmi(admin.ModelAdmin):
	list_display=['name','country']
admin.site.register(mi,Adminmi)
class Adminrr(admin.ModelAdmin):
	list_display=['name','country']
admin.site.register(rr,Adminrr)
class Adminrcb(admin.ModelAdmin):
	list_display=['name','country']
admin.site.register(rcb,Adminrcb)
class Adminsh(admin.ModelAdmin):
	list_display=['name','country']
admin.site.register(sh,Adminsh)