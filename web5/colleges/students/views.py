from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1> this is home page <h2>')
def about(request):
    return HttpResponse('<h1> this is about page <h2>')

# Create your views here.
