from django.shortcuts import render
from iplteamapp.forms import MumbaiForm
# Create your views here.
def homepage(request):

	return render(request,'iplteamapp/homepage.html')

def addperson(request):
	form=MumbaiForm()

	if request.method=="POST":
		form_data=MumbaiForm(request.POST)
		if form_data.is_valid():
			form_data.save(commit=True)

	if request.method=="POST":
		form_data=MumbaiForm(request.POST)
		if form_data.is_valid():
			print("Cricketers details")
			print("Name : ",form_data.cleaned_data['name'])
			print("Age : ",form_data.cleaned_data['age'])
			print("Country : ",form_data.cleaned_data['country'])


	my_dict={'form':form}
	return render(request,'iplteamapp/addperson.html',context=my_dict)

from iplteamapp.models import Mumbaidetails
def display(request):
	display_data=Mumbaidetails.objects.all()
	my_dict={'display_data':display_data}
	return render(request,'iplteamapp/display.html',context=my_dict)

