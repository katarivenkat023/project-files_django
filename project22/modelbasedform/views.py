from django.shortcuts import render
from modelbasedform.forms import StudentForm
# Create your views here.
def thankyou(request):
	return render(request=request,template_name='modelbasedform/thankyou.html')
def modelform(request):
	form=StudentForm()
	my_dict={'form':form}

	if request.method=='POST':
		data_form=StudentForm(request.POST)
		
		if data_form.is_valid():
			print("Student Details")
			print("Name of the student : ",data_form.cleaned_data['name'])
			print('Age of the student : ',data_form.cleaned_data['age'])
			print('Address of the student : ',data_form.cleaned_data['address'])

			data_form.save(commit=True)
			return thankyou(request)

	return render(request=request,template_name='modelbasedform/display.html',context=my_dict)