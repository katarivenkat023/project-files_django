from django.shortcuts import render
from . import forms
# Create your views here.

def student_display(request):
	form=forms.student()
	my_dict={'form':form}
	return render(request,'formapp/display.html',context=my_dict)
