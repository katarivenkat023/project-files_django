from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authenticationapp.forms import SignupForm
from django.http import HttpResponseRedirect
# Create your views here.
def  home_page_view(request):
	return render(request,'authenticationapp/homepage.html')

@login_required
def python_view(request):
	return render(request,'authenticationapp/python.html')

@login_required
def java_view(request):
	return render(request,'authenticationapp/java.html')

@login_required
def testing_view(request):
	return render(request,'authenticationapp/testing.html')

def logout_page(request):
	return render(request,'authenticationapp/logout.html')

def signup_page(request):
	form=SignupForm()
	my_dict={'form':form}
	if request.method=="POST":
		form=SignupForm(request.POST)
		if form.is_valid():
			user=form.save()
			user.set_password(user.password)
			user.save()
		return HttpResponseRedirect('/accounts/login/')
	return render(request,'authenticationapp/signup.html',context=my_dict)
