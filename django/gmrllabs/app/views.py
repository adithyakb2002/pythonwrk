from django.shortcuts import render
 
def index(request):
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
    return render(request,'contactus.html')
def test(request):
    return render(request,'test.html')

# sub pages
def bookanappointment(request):
    return render(request,'bookanappointment.html')
def ayushsilverplan(request):
    return render(request,'ayushsilverplan.html')

# Create your views here.
