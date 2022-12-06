from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(response):
    return render(response, "main/main.html", {})

def news(response):
    return render(response, "main/main.html", {})

def my_game(response):
    return render(response, "main/main.html", {})

def about_us(response):
    return render(response, "main/main.html", {})

def search(response):
    q = response.GET.get('q')
    if q is None:
        q = ''

    context = {
        'q': q,
    }

    return render(response, "main/search.html", context)