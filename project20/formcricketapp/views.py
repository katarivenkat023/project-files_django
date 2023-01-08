from django.shortcuts import render
from . import forms

# Create your views here.
def cricket_display(request):
	form=forms.CricketForm()
	my_dict={'form':form}
	return render(request,'formcricketapp/display.html',context=my_dict)