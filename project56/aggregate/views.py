from django.shortcuts import render
from aggregate.models import Employee
from django.db.models import Q,Avg,Max,Min,Sum,Count
# Create your views here.
def aggregate_view(request):
	avg=Employee.objects.all().aggregate(Avg('esalary'))
	minimum=Employee.objects.all().aggregate(Min('esalary'))
	maximum=Employee.objects.all().aggregate(Max('esalary'))
	total=Employee.objects.all().aggregate(Sum('esalary'))
	count=Employee.objects.all().aggregate(Count('esalary'))

	my_dict={'avg':avg,'min':minimum,'max':maximum,'total':total,'count':count}
	return render(request,'aggregate/display.html',context=my_dict)

