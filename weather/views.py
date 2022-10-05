from django.shortcuts import render

def index(request):
    return render(request, 'weather/index.html')

def test_page(request):
    return render(request, 'weather/test_page.html')
