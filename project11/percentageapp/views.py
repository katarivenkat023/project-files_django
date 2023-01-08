from django.shortcuts import render

# Create your views here.
def student(request):
	name='A.Venkata Subbaiah'
	roll_no= '0316044843'
	college='Sri Srinivasa Degree college'
	year_of_passing=2018
	Percentage='77.4%'
	my_dict={'name':name,'roll_no':roll_no,'college':college,'year_of_passing' :year_of_passing,'Percentage':Percentage,}
	return render(request,'detailsapp/details.html',context=my_dict)