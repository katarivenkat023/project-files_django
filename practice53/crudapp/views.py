from django.shortcuts import render
from crudapp.models import Employee
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class Homepage(TemplateView):
	template_name='crudapp/homepage.html'

class employeelistview(ListView):
	model=Employee

class employeedetailsview(DetailView):
	model=Employee
	fields=('eid','ename','email','ephone_number','esalary','eaddress') 

class employeecreateview(CreateView):
	model=Employee
	fields=('eid','ename','email','ephone_number','esalary','eaddress')

class employeeupdateview(UpdateView):
	model=Employee
	fields=('ename','email','ephone_number','esalary','eaddress')
class employeedeleteview(DeleteView):
	model=Employee
	success_url = reverse_lazy('list')