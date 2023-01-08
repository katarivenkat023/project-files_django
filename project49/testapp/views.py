from django.shortcuts import render
from testapp.models import Book
from django.views.generic import ListView
# Create your views here.
def bookfbv(request):
	book=Book.objects.all()
	my_dict={'book':book}
	return render(request,'testapp/display_fbv.html',context=my_dict)

class bookcbv(ListView):
	model=Book