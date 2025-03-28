from django.shortcuts import render, HttpResponse
import requests
import datetime

# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = "Port Harcourt"
    url: f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=91a016a5ded7f0fd7f29ebb4d50c8090'
    PARAMS = {'units':'metrics'}
    
    data = request.get(url, PARAMS).json()

    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main'][0]['temp']
    
    day = datetime.date.today()
    
    context = {
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day,
    }
    
    return render(request, 'mainapp/index.html', context)