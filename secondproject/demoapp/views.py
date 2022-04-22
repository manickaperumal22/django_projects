from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def gm_view(request):
    return HttpResponse("<h1>good morning</h1>")

def ge_view(request):
    return HttpResponse("<h1>good evening</h1>")

def gn_view(request):
    return HttpResponse("<h1>good night</h1>")