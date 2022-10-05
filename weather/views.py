from django.shortcuts import render
import requests

def index(request):
    appid = "03e783d17d771bd83e3dc0916d5c153c"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=ru&appid=" + appid

    city = "Gomel"
    res = requests.get(url.format(city)).json()
    
    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }

    context = {'info': city_info}

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
