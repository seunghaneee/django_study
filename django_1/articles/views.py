from django.shortcuts import render
import random
# Create your views here.

def index(request):
    return render(request, 'articles/index.html')

def greeting(request):
    foods = ['apple', 'banana', 'coconut']
    info = {
        'name': 'Alice'
        }
    context = {
        'foods': foods,
        'info': info,
    }
    return render(request, 'articles/greeting.html', context)

def dinner(request):
    foods = ['족발', '햄버거', '치킨', '초밥',]
    pick = random.choice(foods)
    context = {
        'foods': foods,
        'pick': pick,
    }
    return render(request, 'articles/dinner.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    # print(request)
    # print(type(request))
    # print(request.GET)
    # print(request.GET.get('message'))
    # raise
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)

def hello(request, name):
    context = {
        'name': name
    }
    return render(request, 'articles/hello.html', context)
