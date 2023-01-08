from django.shortcuts import render,redirect
from bookmyshowapp.models import MovieInfo
from bookmyshowapp.forms import MovieInfoForm

# Create your views here.
def homepage(request):
	return render(request,'bookmyshowapp/homepage.html')

def display(request):
	movie=MovieInfo.objects.all()
	my_dict={'movie':movie}
	return render(request,'bookmyshowapp/display.html',context=my_dict)

def create(request):
	form=MovieInfoForm()
	my_dict={'form':form}
	if request.method=="POST":
		form=MovieInfoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/display/')
	return render(request,'bookmyshowapp/create.html',context=my_dict)

def delete(request,id):
	movie=MovieInfo.objects.get(id=id)
	movie.delete()
	return redirect('/display/')	

def update(request,id):
	movie=MovieInfo.objects.get(id=id)
	my_dict={'movie':movie}
	if request.method=="POST":
		form=MovieInfoForm(request.POST,instance=movie)
		if form.is_valid():
			form.save()
		return redirect('/display/')
	return render(request=request, template_name='bookmyshowapp/update.html',context=my_dict)




