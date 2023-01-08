from django.shortcuts import render
from profileapplicationapp.forms import AgeForm,NameForm,GfForm


# Create your views here.
def name_view(request):
	form=NameForm()
	return render(request,'profileapplicationapp/name.html',{'form':form})

def age_view(request):
	name=request.GET['name']
	request.session['name']=name
	form=AgeForm()

	return render(request,'profileapplicationapp/age.html',{'form':form})

def gf_view(request):
	age=request.GET['age']
	request.session['age']=age
	form=GfForm()

	return render(request,'profileapplicationapp/gf.html',{'form':form})

def result_view(request):
	gf=request.GET['gf']
	request.session['gf']=gf
	return render(request,'profileapplicationapp/results.html')