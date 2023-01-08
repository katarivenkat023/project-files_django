from django.shortcuts import render
from iplteamapp.models import iplteams,csk,dc,kp,kkr,mi,rr,rcb,sh
# Create your views here.
def homepage(request):
	return render(request,'iplteamapp/homepage.html')

def teamdetails(request):
	return render(request,'iplteamapp/teams.html')

def csk_page(request):
	csk_data=csk.objects.all()
	my_dict={'csk_data':csk_data}
	return render(request,'iplteamapp/csk.html',context=my_dict)

def dc_page(request):
	dc_data=dc.objects.all()
	my_dict={'dc_data':dc_data}
	return render(request,'iplteamapp/dc.html',context=my_dict)

def kp_page(request):
	kp_data=kp.objects.all()
	my_dict={'kp_data':kp_data}
	return render(request,'iplteamapp/kp.html',context=my_dict)

def kkr_page(request):
	kkr_data=kkr.objects.all()
	my_dict={'kkr_data':kkr_data}
	return render(request,'iplteamapp/kkr.html',context=my_dict)

def mi_page(request):
	mi_data=mi.objects.all()
	my_dict={'mi_data':mi_data}
	return render(request,'iplteamapp/mi.html',context=my_dict)
def rr_page(request):
	rr_data=rr.objects.all()
	my_dict={'rr_data':rr_data}
	return render(request,'iplteamapp/rr.html',context=my_dict)

def rcb_page(request):
	rcb_data=rcb.objects.all()
	my_dict={'rcb_data':rcb_data}
	return render(request,'iplteamapp/rcb.html',context=my_dict)

def sh_page(request):
	sh_data=sh.objects.all()
	my_dict={'sh_data':sh_data}
	return render(request,'iplteamapp/sh.html',context=my_dict)

