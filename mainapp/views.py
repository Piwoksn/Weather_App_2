from django.shortcuts import render, HttpResponse
import requests
import datetime

# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = "lagos"
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=91a016a5ded7f0fd7f29ebb4d50c8090'
    
    PARAMS = {'units': 'metric'}  
    
    response = requests.get(url, params=PARAMS)
    data = response.json()

    if response.status_code == 200:  
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

        day = datetime.date.today()

        context = {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city
        }
    else:
        context = {'error': 'City not found. Please try again.'}

    return render(request, 'mainapp/index.html', context)
