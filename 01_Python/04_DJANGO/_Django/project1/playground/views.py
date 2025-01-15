from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# def say_hello(request):
#    return HttpResponse("Hello World")

def calculator():
    x = 5 
    y = 10 
    return x


def say_hello(request):
    x = calculator()
    y = 2 
    return render(request, 'hello.html', {'name': 'Mosh'})
