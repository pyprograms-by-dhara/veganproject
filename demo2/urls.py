"""demo2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from demo2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('gallery/', views.gallery),
    path('menu/', views.menu),
    path('punjabi/', views.punjabi),
    path('soup/', views.soup),
    path('salad/', views.salad),
    path('stater/', views.stater),
    path('south/', views.south),
    path('gujrati/', views.gujrati),
    path('chienese/', views.chienese),
    path('softdrink/', views.softdrink),
    path('aboutus/', views.aboutus),
    path('contactus/', views.contactus),
    path('booking/', views.booking),
    path('thanks/',views.thanks)
]
