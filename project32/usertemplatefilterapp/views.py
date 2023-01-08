from django.shortcuts import render
from usertemplatefilterapp.models import UserTemplateFilter
# Create your views here.

def user_templatefilter(request):
	data=UserTemplateFilter.objects.all()
	my_dict={'data':data}
	return render(request=request, template_name='usertemplatefilterapp/usertemplatefilter.html',context=my_dict)