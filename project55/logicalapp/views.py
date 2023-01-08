from django.shortcuts import render
from logicalapp.models import Employee
from django.db.models import Q
# Create your views here.
def and_view(request):
	emp=Employee.objects.filter(ename__startswith='k',esalary__gt=200000)
	#emp=Employee.objects.filter(ename__startswith='k' & esalary__gt=200000)
	#emp=Employee.objects.filter(Q(ename__startswith='k') & Q(esalary__gt=200000))
	my_dict={'emp':emp}
	return render(request,'logicalapp/and.html',context=my_dict)

def or_view(request):
	emp=Employee.objects.filter(Q(ename__startswith='k')|Q(esalary__gt=200000))
	#emp=Employee.objects.filter(Q(ename__startswith='k')|Employee.objects.filter(Q(esalary__gt=200000))
	my_dict={'emp':emp}
	return render(request,'logicalapp/or.html',context=my_dict)

def not_view(request):
	emp=Employee.objects.filter(~Q(ename__startswith='k'))
	#emp=Employee.objects.exclude(ename__startswith='k')
	my_dict={'emp':emp}
	return render(request,'logicalapp/not.html',context=my_dict)