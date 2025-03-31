from django.shortcuts import render, HttpResponse
import requests
import datetime

# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = "lagos"
    
    # City url (Google search engine)
    api_key ="AIzaSyCkgEmVtuqJ1Dqzj_qvUu5s2-DIuJOuSXY"
    cse_id = "90ee7e8f4659d4b21"
    query = f"{city} 1920x1080"
    page = 1
    start = (page-1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={cse_id}&key={api_key}&start={start}&searchType={searchType}"
    city_data = requests.get(city_url).json()
    search_items = city_data.get("items")
    image_url = search_items[2]['link']
    
    print(image_url)
    
    # weather -----
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
            'city': city, 
            'image':image_url,
        }
    else:
        context = {'error': 'City not found. Please try again.'}

    return render(request, 'mainapp/index.html', context)