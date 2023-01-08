from django.shortcuts import render
from testapp.models import Book
from django.views.generic import DetailView
# Create your views here.


class bookcbv(DetailView):
	model=Book