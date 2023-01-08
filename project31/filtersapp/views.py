from django.shortcuts import render
from filtersapp.models import studentdetails
# Create your views here.
def upper_info(request):
	data=studentdetails.objects.all()
	my_dict={'data':data}
	return render(request,'filtersapp/upper.html',my_dict)
def lower_info(request):
	data=studentdetails.objects.all()
	my_dict={'data':data}
	return render(request,'filtersapp/lower.html',my_dict)