from django.shortcuts import render,redirect
from . models import *
def index(request):
    context={}
    
    obj=Packages.objects.all()
    context['obj']=obj

    if request.method=='POST':
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

def newsevents(request):
    context={}
    
    obj=Newsevents.objects.all()
    context['obj']=obj
    return render(request,'newsevents.html',context)

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
            # print(details)
            return  redirect('contactus')
    return render(request,'contactus.html')


def gallery(request):
    context={}
    
    obj=Gallery.objects.all()
    context['obj']=obj
    return render(request,'gallery.html',context)

# subpages
def subpackages(request,id):
    context={}

    obj=Packages.objects.all()
    plan=Subpackages.objects.filter(package=id)
    context['plan']=plan
    context['obj']=obj
    return render(request,'subpackages.html',context)

def subpackagesinner(request,id):
    context={}

    obj=Packages.objects.all()
    plan=Subpackagesinner.objects.filter(package=id)
    context['plan']=plan
    context['obj']=obj
    return render(request,'subpackagesinner.html',context)
    
def subnewsevents(request):
    return render(request,'subnewsevents.html')



# Create your views here.
