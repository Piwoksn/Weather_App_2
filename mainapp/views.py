from django.shortcuts import render, HttpResponse
import requests
import datetime

# Create your views here.
def home(request):
    url: f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=91a016a5ded7f0fd7f29ebb4d50c8090'
    return render(request, 'mainapp/index.html')