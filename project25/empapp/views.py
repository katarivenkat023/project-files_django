
from django.shortcuts import render
from empapp.forms import EmployeeForm

# Create your views here.
def homepage(request):
	return render(request,'empapp/homepage.html')

def register(request):
	
	if request.method=="GET":
		form=EmployeeForm()
		my_dict={'form':form}
	if request.method=="POST":
		form=EmployeeForm(request.POST)
		my_dict={'form':form}
		if form.is_valid():
			print("Employee details")
			print('Employee Id: ',form.cleaned_data['emp_id'])
			print('Employee Name : ',form.cleaned_data['name'])
			print('Employee email: ',form.cleaned_data['email'])
			print("Employee address: ",form.cleaned_data['address'])

			return success(request)

	return render(request,'empapp/register.html',context=my_dict)

def success(request):
	return render(request,'empapp/success.html')