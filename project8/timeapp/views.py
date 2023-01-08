from django.shortcuts import render
from datetime import datetime
# Create your views here.
def display_time(request):
	server_time=datetime.now()
	my_dict={'time':server_time}
	return render(request,'timeapp/time.html',context=my_dict)