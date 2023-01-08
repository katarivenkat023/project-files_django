from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Welcome(TemplateView):
	template_name='contextapp/welcome.html'
	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		context['name']="venky"
		context['subject']='python'
		context['marks']=99
		return context