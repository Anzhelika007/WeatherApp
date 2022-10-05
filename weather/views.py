from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    appid = "03e783d17d771bd83e3dc0916d5c153c"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=ru&appid=" + appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()  
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }
        if city_info not in all_cities:
            all_cities.append(city_info)
        else:
            index = all_cities.index(city_info)
            desc = all_cities.pop(index)
            all_cities.insert(0, desc)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)

    


def test_page(request):
    appid = "03e783d17d771bd83e3dc0916d5c153c"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=ru&appid=" + appid

    city = "Gomel"
    res = requests.get(url.format(city)).json()
    
    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'description': res["weather"][0]["description"]
    }

    context = {'info': city_info}
    
    return render(request, 'weather/test_page.html', context)
