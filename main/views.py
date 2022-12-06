from django.http import HttpResponse, request
from django.shortcuts import render

# Create your views here.

def home(response):
    try:
        q = request.GET.get('q')
    except:
        q = ''

    # else:
    #     q = ''

    context = {

    }

    return render(response, "main/main.html", context)

def news(response):
    return render(response, "main/main.html", {})

def my_game(response):
    return render(response, "main/main.html", {})

def about_us(response):
    return render(response, "main/main.html", {})

def search(response):
    return render(response, "main/main.html", {})