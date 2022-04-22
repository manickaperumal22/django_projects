from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def one(request):
    return HttpResponse("<h1>one </h1>")

def two(request):
    return HttpResponse("<h1>two </h1>")

def three(request):
    return HttpResponse("<h1>three </h1>")

def four(request):
    return HttpResponse("<h1>four </h1>")