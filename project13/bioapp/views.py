from django.shortcuts import render

# Create your views here.
def home(request):
	name="A Venkata Subbaiah"
	return render(request,'bioapp/home.html',context={'name':name})

def ssc_page(request):
	name="A Venkata Subbaiah"
	school="Hope High school"
	percentage="83%"
	return render(request,'bioapp/ssc.html',context={'name':name,'percentage':percentage,'school':school})

def puc_page(request):
	name="A Venkata Subbaiah"
	college="Sri Viswasadhana Jr college"
	group="M.P.C"
	percentage="71%"
	return render(request,'bioapp/puc.html',context={'name':name,'percentage':percentage,'college':college,'group':group})
def degree_page(request):
	name="A Venkata Subbaiah"
	college="Sri Srinivasa Degree college"
	group="B.Sc (MSCS)"
	percentage="78%"

	return render(request,'bioapp/degree.html',context={'name':name,'percentage':percentage,'college':college,'group':group})
