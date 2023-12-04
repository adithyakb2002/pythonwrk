from django.shortcuts import render
from . models import *

def index(request):
    author=Author.objects.all()
    return render (request,'index.html',{'author':author})
# Create your views here.
