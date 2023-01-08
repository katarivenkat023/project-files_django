from django.shortcuts import render
from dateapp.forms import LoginForm
import datetime
# Create your views here.
def home_page(request):
	form=LoginForm()
	my_dict={'form':form}
	return render(request=request, template_name='dateapp/homepage.html',context=my_dict)


def collect_cookie(request):
	#collecting the data from end user
	name=request.GET['name']
	my_dict={'name':name}
	response=render(request=request, template_name='dateapp/collectcookie.html',context=my_dict)

	# set_cookie('cookiename','cookievalue')
	response.set_cookie('name',name)
	return response

def display_time(request):
	name=request.COOKIES['name']
	data=datetime.datetime.now()
	my_dict={'name':name,'data':data}
	return render(request=request, template_name='dateapp/displaytime.html',context=my_dict)



