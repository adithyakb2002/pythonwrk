from django.shortcuts import render
from .models import *

def index(request):
    student=Student.objects.all()
    return render(request,'index.html',{'student':student})

# Create your views here.
