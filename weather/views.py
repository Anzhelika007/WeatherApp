from django.shortcuts import render
import requests

def index(request):
    appid = "03e783d17d771bd83e3dc0916d5c153c"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    city = "Gomel"
    res = requests.get(url.format(city))
    print(res.text)

    return render(request, 'weather/index.html')

    


def test_page(request):
    return render(request, 'weather/test_page.html')
