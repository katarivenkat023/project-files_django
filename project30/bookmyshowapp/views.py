from django.shortcuts import render

# Create your views here.
def homepage(request):
	return render(request,'bookmyshowapp/homepage.html')

def movies(request):
	return render(request,'bookmyshowapp/moviespage.html')
	
def sports(request):
	return render(request,'bookmyshowapp/sportspage.html')


def events(request):
	return render(request,'bookmyshowapp/eventspage.html')
	