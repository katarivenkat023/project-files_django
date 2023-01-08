from django.urls import path
from bioapp import views
urlpatterns=[
	path('home/',views.home),
	path('ssc/',views.ssc_page),
	path('puc/',views.puc_page),
	path('degree/',views.degree_page),
]