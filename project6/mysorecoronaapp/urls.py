
from mysorecoronaapp import views as mysore
from django.urls import path

urlpatterns = [
    path('vijayanagar/',mysore.corona_vijayanagar),
    path('kdroad/',mysore.corona_kdroad),
    path('ramakarishananagar/',mysore.corona_ramakrishnanagar),
]
