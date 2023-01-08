from django.shortcuts import render
from testapp.models import Book
from django.views.generic import ListView
# Create your views here.


class bookcbv(ListView):
	model=Book
	#customised template
	template_name='testapp/display.html'

	#customised key
	context_objects_name='list_of_books'