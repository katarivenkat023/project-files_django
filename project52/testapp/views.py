from django.shortcuts import render
from testapp.models import Book
from django.views.generic import ListView,DetailView
# Create your views here.


class booklistcbv(ListView):
	model=Book


class bookdetailcbv(DetailView):
	model=Book