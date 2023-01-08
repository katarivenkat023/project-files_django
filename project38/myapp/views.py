from django.shortcuts import render
from myapp.forms import LoginForm
# Create your views here.
def name_info(request):
	
	return render(request=request, template_name='myapp/name.html',)

def age_info(request):
	name=request.GET['name']
	response=render(request=request, template_name='myapp/age.html')
	response.set_cookie('name',name)
	return response

def gf_info(request):
	age=request.GET['age']
	response=render(request=request, template_name='myapp/gf.html')
	response.set_cookie('age',age)
	return response

def display(request):
	gf=request.GET['gf']
	name=request.COOKIES.get('name')
	age=request.COOKIES.get('age')
	my_dict={'name':name,'age':age,'gf':gf}
	response=render(request=request, template_name='myapp/display.html',context=my_dict)
	return response



from django.shortcuts import render

# Create your views here.
def name_info(request):
	return render(request=request, template_name='name.html')

def age_info(request):
	name=request.GET['name']
	response=render(request=request, template_name='age.html')
	response.set_cookie('name',name)
	return response

def gf_info(request):
	age=request.GET['age']
	response=render(request=request, template_name='gf.html')
	response.set_cookie('age',age)
	return response

def display(request):
	gf=request.GET['gf']
	name=request.COOKIES.get['name']
	age=request.COOKIES.get['age']
	my_dict={'name':name,'age':age,'gf':gf}
	response=render(request=request, template_name='display.html',context=my_dict)
	return response
	 	
