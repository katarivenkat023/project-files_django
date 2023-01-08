from django.shortcuts import render
import datetime

# Create your views here.
def wish(request):
	date=datetime.datetime.now()
	hour=int(datetime.datetime.now().hour)
	msg='Welcome to study online... Good  '
	if hour >0:
		msg=msg+"Morning"
	elif hour>12:
		msg=msg+"Afternoon" 
	elif hour>16:
		msg=msg+"Evening"
	else:
		msg=msg+"Night"
	
	my_dict={'insert_date':date,'insert_msg':msg}
	
	return render(request,'timeapp/time.html',context=my_dict)