from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Welcome(TemplateView):
	template_name='tempViewapp/welcome.html'
