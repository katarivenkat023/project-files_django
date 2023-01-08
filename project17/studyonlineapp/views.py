from django.shortcuts import render
from studyonlineapp.models import studyonline
# Create your views here.
def home(request):
	return render(request,'studyonlineapp/homepage.html')
def display(request):
	student_data=studyonline.objects.all()
	my_dict={'student_data':student_data}
	return render(request,'studyonlineapp/display.html',context=my_dict)