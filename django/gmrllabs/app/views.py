from django.shortcuts import render
 
def index(request):
    return render(request,'index.html')
def aboutus(request):
    return render(request,'aboutus.html')
def packages(request):
    return render(request,'packages.html')
def department(request):
    return render(request,'department.html')

# Create your views here.
