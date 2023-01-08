from django.shortcuts import render
from inbuiltapp.forms import StudentForm
# Create your views here.

def homepage(request):
	return render(request,'inbuiltapp/homepage.html')

def student(request):
	
	if request.method=="GET":
		form=StudentForm()
		my_dict={'form':form}
	if request.method=="POST":
		form=StudentForm(request.POST)
		my_dict={'form':form}
		if form.is_valid():
			print("student details")
			print('Name : ',form.cleaned_data['name'])
			print('rollno : ',form.cleaned_data['rollno'])
			print('email: ',form.cleaned_data['email'])
			print('address: ',form.cleaned_data['address'])

			return thankyou(request)
	
	return render(request,'inbuiltapp/register.html',context=my_dict)

def thankyou(request):
	return render(request,'inbuiltapp/thanks.html')