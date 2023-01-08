"""project5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from bangalorecoronaapp import views as bangalore
from hassancoronaapp import views as hassan
from mysorecoronaapp import views as mysore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bangalore/vijayanagar/',bangalore.corona_vijayanagar),
    path('bangalore/btm/',bangalore.corona_btm),
    path('bangalore/hebbal/',bangalore.corona_hebbal),

    path('hassan/sathyamanagala/',hassan.corona_sathyamangala),
    path('hassan/chennarayapatna/',hassan.corona_chennarayapatna),
    path('hassan/arsikere/',hassan.corona_arsikere),

    path('mysore/vijayanagar/',mysore.corona_vijayanagar),
    path('mysore/kdroad/',mysore.corona_kdroad),
    path('mysore/ramakarishananagar/',mysore.corona_ramakrishnanagar),
]
