from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from vegan.models import book

def home(request):
    return render(request,"rindex.htm")

def gallery(request):
    return render(request,"rgallery.htm")

def menu(request):
    return render(request,"menu.htm")

def punjabi(request):
    return render(request,"punjabi.htm")

def soup(request):
    return render(request,"soup.htm")

def stater(request):
    return render(request,"statermenu.htm")

def south(request):
    return render(request,"south.htm")

def salad(request):
    return render(request,"saladmenu.htm")

def gujrati(request):
    return render(request,"gujrati.htm")

def chienese(request):
    return render(request,"chienese.htm")

def softdrink(request):
    return render(request,"softdrink.htm")

def aboutus(request):
    return render(request,"raboutus.htm")

def contactus(request):
    return render(request,"contact.htm")
    
def booking(request):
    return render(request,"booking.htm")

def thanks(request):
    msg='--'
    if request.method=="POST":
        name=request.POST.get('nm')
        email=request.POST.get('email')
        phone=request.POST.get('no')
        person=request.POST.get('person')
        date=request.POST.get('date')
        saverecord=book(name=name,email=email,phone=phone,person=person,date=date)
        saverecord.save()
        msg="Your table registered successfully"
    return render(request,"thanks.htm",{'output':msg})