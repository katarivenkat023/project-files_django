
from hassancoronaapp import views as hassan
from django.urls import path

urlpatterns = [

    path('sathyamanagala/',hassan.corona_sathyamangala),
    path('chennarayapatna/',hassan.corona_chennarayapatna),
    path('arsikere/',hassan.corona_arsikere),
]
