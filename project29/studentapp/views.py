from django.shortcuts import render
from studentapp.forms import StudentForm

# Create your views here.
def home_page(request):
	return render(request=request, template_name='studentapp/homepage.html')

def thank_you(request):
	return render(request=request, template_name='studentapp/thankyou.html')

def feedback_data(request):
	if request.method=='GET':
		form=StudentForm()
		my_dict={'form':form}

	if request.method=='POST':
		form=StudentForm(request.POST)
		my_dict={'form':form}
		if form.is_valid():
			print('Data Enterted by Study Online Student')
			print('Name:',form.cleaned_data['name'])
			print('Mail Id :',form.cleaned_data['mail_id'])
			print('Password :',form.cleaned_data['password'])
			print('Again Password :',form.cleaned_data['re_password'])
			print('Trainer Name :',form.cleaned_data['trainer_name'])
			print('Feedback:',form.cleaned_data['feedback'])
			return thank_you(request)

	return render(request=request, template_name='studentapp/feedback.html',context=my_dict)
