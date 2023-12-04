from django.shortcuts import render
from . models import *
from . forms import *
 

def index(request):
    context={}
    lemon=Lemon.objects.all()
    lemon_form=Lemon_form()

    if request.method=="POST":
        if 'save' in request .POST:
            lemon_form=Lemon_form(request.POST)
            lemon_form.save()
           
    
    context['lemon']=lemon
    context['lemon_form']=lemon_form
    return render(request,'index.html',context) 

# Create your views here.
