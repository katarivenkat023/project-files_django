from django.shortcuts import render
from customefilterapp.models import employeedetails
# Create your views here.
def empdata(request):
	data=employeedetails.objects.all()
	my_dict={'data':data}
	return render(request,'customefilterapp/customfilter.html',context=my_dict)