from django.shortcuts import render,redirect
from . models import *



def index(request):
    context={}

    obj=Packages.objects.all()
    context['obj']=obj
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')

        if request.POST:
            details=Index.objects.create(name=name,email=email,phone=phone,message=message)
            details.save()
            return  redirect('index')
    return render(request,'index.html',context)


def aboutus(request):
    return render(request,'aboutus.html')

def packages(request):
    context={}

    obj=Packages.objects.all()
    context['obj']=obj
    return render(request,'packages.html',context)


def department(request):
    return render(request,'department.html')

def blog(request):
    context={}

    obj=Packages.objects.all()
    context['obj']=obj
    return render(request,'blog.html',context)

def gallery(request):
    context={}

    obj=Gallery.objects.all()
    context['obj']=obj
    return render(request,'gallery.html',context)

def branches(request):
    context={}

    obj=Branches.objects.all()
    context['obj']=obj
    return render(request,'branches.html',context)




def contactus(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        if request.POST:
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

def ayushsilverplan(request,id):
    context={}

    obj=Packages.objects.all()
    plan=Ayushsilverplan.objects.filter(package=id)
    context['plan']=plan
    context['obj']=obj
    return render(request,'ayushsilverplan.html',context)



def subblog(request):
    return render(request,'subblog.html')


# Create your views here.
