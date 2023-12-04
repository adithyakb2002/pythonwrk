from django.shortcuts import render
import requests

def index(request):
    context={}
    api='42a8e44e2b241e55b2708a4822ff984b'
    city='kochi'
    if request.method=="POST":
        city=request.POST.get('city')
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city }&appid={api}&units=metric'    
    response=requests.get(url)
    data=response.json()
    weather=data['weather'][0]['description']
    temp=data['main']['temp']
    temp_max=data['main']['temp_max']
    temp_min=data['main']['temp_min']

    context['city']=city
    context['temp']=temp
    context['temp_max']=temp_max
    context['temp_min']=temp_min

    context['weather']=weather
    return render (request,'index.html',context)
# Create your views here.
