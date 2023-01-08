from django.shortcuts import render
from studentapp.forms import StudentForm
# Create your views here.
def home_page(request):
	return render(request=request, template_name='studentapp/homepage.html')

def thank_you(request):
	return render(request=request, template_name='studentapp/thankyou.html')

def register_data(request):
	if request.method=='GET':
		form=StudentForm()x
		
		my_dict={'form':form}
		return render(request=request, template_name='studentapp/register.html',context=my_dict)

	if request.method=='POST':
		form=StudentForm(request.POST)
		my_dict={'form':form}
		if form.is_valid():
			print('Data Enterted by Study Online Student')
			print('Name:',form.cleaned_data['name'])
			print('Password:',form.cleaned_data['password'])
			print('RE-Password:',form.cleaned_data['re_password'])
			print('ID:',form.cleaned_data['studyonline_id'])
			print('MAIL ID :',form.cleaned_data['mail_id'])
			print('MOBILE NUMBER',form.cleaned_data['phone_number'])
			print('FEEDBACK:',form.cleaned_data['feedback'])
		
			return thank_you(request)

	return render(request=request, template_name='studentapp/register.html',context=my_dict)