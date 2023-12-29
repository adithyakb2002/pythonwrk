from django.shortcuts import render,redirect
from . models import *



def index(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')

        if request.POST:
            details=Index.objects.create(name=name,email=email,phone=phone,message=message)
            details.save()
            return  redirect('index')
    return render(request,'index.html')


def aboutus(request):
    return render(request,'aboutus.html')
def packages(request):
    return render(request,'packages.html')
def department(request):
    return render(request,'department.html')
def blog(request):
    return render(request,'blog.html')
def gallery(request):
    return render(request,'gallery.html')
def branches(request):
    return render(request,'branches.html')




def contactus(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        if request.POST:
            # print(message)
            details=Contact.objects.create(name=name,email=email,phone=phone,message=message,subject=subject)
            details.save()
            return  redirect('contactus')
    return render(request,'contactus.html')



def test(request):
    return render(request,'test.html')
# sub pages
def bookanappointment(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        date=request.POST.get('date')
        time=request.POST.get('time')
        age=request.POST.get('age')
        address=request.POST.get('address')
        gender=request.POST.get('gender')

        if request.POST:
            details=Appointment.objects.create(name=name,email=email,phone=phone,message=message,date=date,time=time,age=age,address=address,gender=gender)
            details.save()
            return  redirect('bookanappointment')
    return render(request,'bookanappointment.html')


def ayushsilverplan(request):
    return render(request,'ayushsilverplan.html')

# Create your views here.
